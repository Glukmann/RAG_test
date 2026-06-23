# Деплой RAG-системы на Ubuntu-сервер

Инструкция по развёртыванию системы на удалённом сервере с Ubuntu и Docker.

## Требования к серверу

- Ubuntu 22.04 LTS или новее
- Docker Engine + Docker Compose plugin
- Git
- Пользователь с правами `docker`
- Открытые порты: `8000` (ChromaDB), `8002` (MCP), `8080` (Admin UI)
  - или только `8002` и `8080`, если ChromaDB не нужен снаружи

## Быстрый старт

1. Подключитесь к серверу по SSH:
   ```bash
   ssh user@<server-ip>
   ```

2. Убедитесь, что Docker установлен:
   ```bash
   docker --version
   docker compose version
   ```

3. Скачайте и запустите скрипт настройки:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/Glukmann/RAG_test/main/deploy/ubuntu-setup.sh -o /tmp/ubuntu-setup.sh
   chmod +x /tmp/ubuntu-setup.sh
   /tmp/ubuntu-setup.sh
   ```

   Или вручную:
   ```bash
   git clone https://github.com/Glukmann/RAG_test.git ~/rag
   cd ~/rag
   cp .env.example .env
   # отредактируйте .env, укажите безопасные токены
   docker compose up --build -d
   ```

## Что делает скрипт

1. Клонирует/обновляет репозиторий в `~/rag`.
2. Создаёт `.env` со случайными токенами.
3. Собирает и запускает контейнеры.
4. Проверяет healthcheck MCP и ChromaDB.
5. Создаёт systemd user-сервис `rag.service` для автозапуска.

## После деплоя

| Сервис | URL | Примечание |
|--------|-----|------------|
| ChromaDB API | `http://<server-ip>:8000` | Bearer `CHROMA_TOKEN` |
| Admin UI | `http://<server-ip>:8080?token=<ADMIN_API_TOKEN>` | Веб-интерфейс |
| MCP Server | `http://<server-ip>:8002/mcp` | Bearer `MCP_AUTH_TOKEN` |

### Подключение Kimi Code с клиентской машины

```bash
kimi mcp add --transport http chroma-rag http://<server-ip>:8002/mcp \
  --header "Authorization: Bearer <MCP_AUTH_TOKEN>"
```

## Проверка работоспособности

```bash
# ChromaDB
curl http://<server-ip>:8000/api/v1/heartbeat

# MCP
curl http://<server-ip>:8002/health

# Admin UI
curl "http://<server-ip>:8080/api/search?q=test&token=<ADMIN_API_TOKEN>"
```

## Обновление

```bash
cd ~/rag
git pull origin main
docker compose down
docker compose up --build -d
```

## Обновление базы знаний

База знаний хранится в ветке `knowledge` того же репозитория. Для обновления:

1. Добавьте/измените файлы в `https://github.com/Glukmann/RAG_test.git` ветка `knowledge`.
2. В Admin UI нажмите **Pull & Reindex** или выполните:
   ```bash
   curl -X POST "http://<server-ip>:8080/api/reindex?token=<ADMIN_API_TOKEN>"
   ```

## Безопасность

- Замените сгенерированные токены на свои перед продакшеном.
- Не выставляйте порт `8000` наружу, если ChromaDB нужен только внутри Docker-сети.
- Для продакшена настройте reverse proxy (nginx/traefik) с TLS.
- Регулярно бэкапьте Docker volume `chroma-data`:
  ```bash
  docker run --rm -v rag_chroma-data:/data -v $(pwd):/backup alpine \
    tar czf /backup/chroma-backup-$(date +%Y%m%d).tar.gz -C /data .
  ```

## Устранение неполадок

```bash
# Статус контейнеров
docker compose ps

# Логи
docker compose logs -f

# Статус автозапуска
systemctl --user status rag.service

# Перезапуск сервисов
systemctl --user restart rag.service
```
