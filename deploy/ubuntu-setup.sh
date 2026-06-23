#!/bin/bash
set -e

# Скрипт развёртывания RAG-системы на Ubuntu-сервере с Docker.
# Запускать от имени пользователя с правами docker (не root).

PROJECT_DIR="${HOME}/rag"
REPO_URL="https://github.com/Glukmann/RAG_test.git"

# --- Открытие портов в фаерволе ---
if command -v ufw >/dev/null 2>&1; then
    echo "Открываем порты в ufw..."
    sudo ufw allow 8000/tcp >/dev/null 2>&1 || true
    sudo ufw allow 8002/tcp >/dev/null 2>&1 || true
    sudo ufw allow 8080/tcp >/dev/null 2>&1 || true
    sudo ufw reload >/dev/null 2>&1 || true
    echo "Порты открыты в ufw."
fi

# --- Проверка зависимостей ---
command -v docker >/dev/null 2>&1 || { echo "Docker не найден. Установите Docker и Docker Compose plugin."; exit 1; }
command -v git >/dev/null 2>&1 || { echo "Git не найден. Установите: sudo apt-get install git"; exit 1; }

if ! docker info >/dev/null 2>&1; then
    echo ""
    echo "ОШИБКА: текущий пользователь не имеет прав доступа к Docker."
    echo "Выполните следующие команды и перезапустите скрипт:"
    echo ""
    echo "  sudo usermod -aG docker \$USER"
    echo "  newgrp docker"
    echo ""
    exit 1
fi

# --- Клонирование или обновление проекта ---
if [ -d "${PROJECT_DIR}/.git" ]; then
    echo "Проект уже существует, обновляем..."
    cd "${PROJECT_DIR}"
    git pull origin main
else
    echo "Клонируем проект..."
    git clone "${REPO_URL}" "${PROJECT_DIR}"
    cd "${PROJECT_DIR}"
fi

# --- Создание .env ---
if [ ! -f ".env" ]; then
    echo "Создаём .env из шаблона..."
    cp .env.example .env

    # Генерация случайных токенов
    CHROMA_TOKEN="$(openssl rand -hex 32)"
    ADMIN_TOKEN="$(openssl rand -hex 32)"
    MCP_TOKEN="$(openssl rand -hex 32)"

    sed -i "s|^CHROMA_TOKEN=.*|CHROMA_TOKEN=${CHROMA_TOKEN}|" .env
    sed -i "s|^ADMIN_API_TOKEN=.*|ADMIN_API_TOKEN=${ADMIN_TOKEN}|" .env
    sed -i "s|^MCP_AUTH_TOKEN=.*|MCP_AUTH_TOKEN=${MCP_TOKEN}|" .env

    echo ""
    echo "=== Сгенерированы токены (сохраните их) ==="
    echo "CHROMA_TOKEN: ${CHROMA_TOKEN}"
    echo "ADMIN_API_TOKEN: ${ADMIN_TOKEN}"
    echo "MCP_AUTH_TOKEN: ${MCP_TOKEN}"
    echo "============================================"
    echo ""
else
    echo ".env уже существует, пропускаем генерацию токенов."
fi

# --- Запуск сервисов ---
echo "Запускаем Docker Compose..."
docker compose down 2>/dev/null || true
docker compose up --build -d

# --- Проверка здоровья ---
echo "Ожидаем запуска сервисов..."

for i in $(seq 1 30); do
    HEALTH_MCP=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8002/health || true)
    HEALTH_CHROMA=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/api/v1/heartbeat || true)

    echo "Попытка $i: MCP=${HEALTH_MCP}, ChromaDB=${HEALTH_CHROMA}"

    if [ "${HEALTH_MCP}" = "200" ] && [ "${HEALTH_CHROMA}" = "200" ]; then
        echo "Все сервисы доступны."
        break
    fi

    sleep 2
done

if [ "${HEALTH_MCP}" != "200" ] || [ "${HEALTH_CHROMA}" != "200" ]; then
    echo ""
    echo "ВНИМАНИЕ: один из сервисов не отвечает."
    echo "Логи ChromaDB:"
    docker compose logs --tail=30 chromadb
    echo ""
    echo "Логи MCP:"
    docker compose logs --tail=30 mcp-server
    echo ""
    echo "Для постоянного мониторинга: docker compose logs -f"
    exit 1
fi

# --- Настройка автозапуска через systemd ---
echo "Настраиваем автозапуск через systemd..."

mkdir -p "${HOME}/.config/systemd/user"

cat > "${HOME}/.config/systemd/user/rag.service" <<EOF
[Unit]
Description=RAG ChromaDB services
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=${PROJECT_DIR}
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
TimeoutStartSec=0

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable rag.service
systemctl --user start rag.service

echo ""
echo "=== Деплой завершён ==="
echo "ChromaDB API: http://<server-ip>:8000"
echo "Admin UI:      http://<server-ip>:8080?token=<ADMIN_API_TOKEN>"
echo "MCP Server:    http://<server-ip>:8002/mcp"
echo ""
echo "Для подключения Kimi Code на клиентской машине:"
echo "  kimi mcp add --transport http chroma-rag http://<server-ip>:8002/mcp \\"
echo "    --header \"Authorization: Bearer <MCP_AUTH_TOKEN>\""
echo ""
echo "Логи: docker compose logs -f"
