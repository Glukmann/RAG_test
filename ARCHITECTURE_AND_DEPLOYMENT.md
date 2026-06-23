# Архитектура, развёртывание и подключение RAG-системы на базе ChromaDB

Полное руководство по устройству системы, её настройке, запуску и интеграции с Kimi Code.

---

## 1. Общее описание

Система представляет собой централизованную векторную базу знаний для команды разработчиков. Она позволяет:

- индексировать документацию и примеры кода из Git-репозитория;
- хранить эмбеддинги и метаданные в ChromaDB;
- выполнять семантический поиск через MCP-инструменты в Kimi Code;
- управлять индексацией и мониторить состояние через веб-интерфейс.

### Основные характеристики

| Параметр | Значение |
|----------|----------|
| Язык разработки | Python 3.12 |
| Векторная БД | ChromaDB 0.6.3 |
| Модель эмбеддингов | `all-MiniLM-L6-v2` (384-мерные векторы) |
| MCP-транспорт | Streamable HTTP |
| Контейнеризация | Docker Compose |
| Основная коллекция | `lang_docs` |

---

## 2. Архитектура

### 2.1. Компоненты

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Kimi Code (клиент)                          │
│         search_docs / search_api_reference / get_example_code       │
└───────────────────────────────┬─────────────────────────────────────┘
                                │ HTTP / MCP
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         RAG MCP Server                              │
│   Порт: 3000 (внутри контейнера) / 8002 (на хосте)                  │
│   Токен: MCP_AUTH_TOKEN                                             │
└───────────────────────────────┬─────────────────────────────────────┘
                                │ HTTP API + Bearer token
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         ChromaDB Server                             │
│   Порт: 8000                                                        │
│   Токен: CHROMA_TOKEN                                               │
│   Хранилище: Docker volume chroma-data                              │
└─────────────────────────────────────────────────────────────────────┘
                                ▲
                                │ HTTP API + Bearer token
┌───────────────────────────────┴─────────────────────────────────────┐
│                         Indexer (сервис индексации)                 │
│   Порт: 8001                                                        │
│   Задачи: git pull → чанкинг → эмбеддинги → загрузка в ChromaDB     │
└─────────────────────────────────────────────────────────────────────┘
                                ▲
                                │ HTTP POST /reindex
┌───────────────────────────────┴─────────────────────────────────────┐
│                         Admin UI (веб-интерфейс)                    │
│   Порт: 8080                                                        │
│   Токен: ADMIN_API_TOKEN                                            │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2. Описание компонентов

#### ChromaDB Server (`chroma/`)

- Базовый образ: `chromadb/chroma:0.6.3`.
- Персистентное хранилище данных в Docker volume `chroma-data`.
- Аутентификация по статическому Bearer-токену (`CHROMA_TOKEN`).
- Ограничение памяти: 4 ГБ.
- Healthcheck: `GET /api/v1/heartbeat`.

#### Indexer (`indexer/`)

- FastAPI-приложение с двумя режимами запуска:
  - `python -m indexer.main run` — однократная индексация;
  - `python -m indexer.main api` — запуск HTTP API.
- Поддерживаемые форматы: `.md`, `.txt`, `.rst`, `.mdx`, `.mac` и другие текстовые.
- Чанкинг:
  - документация — по заголовкам;
  - код — по функциям/блокам без разрезания.
- Метаданные чанков: `source`, `doc_type`, `language`, `chunk_index`, `file_ext`, `version`.
- Endpoints:
  - `POST /reindex` — запуск полного цикла обновления;
  - `GET /health` — проверка доступности.

#### MCP Server (`mcp_server/`)

- Реализован на `FastMCP` с транспортом `streamable-http`.
- Подключается к ChromaDB по внутренней сети Docker.
- Предоставляет только read-only инструменты:
  - `search_docs(query, doc_type, n_results)`;
  - `search_api_reference(query, n_results)`;
  - `get_example_code(query, n_results)`.
- Аутентификация по `MCP_AUTH_TOKEN`.
- Endpoints:
  - `GET /health` — проверка здоровья;
  - `POST /mcp` — MCP-эндпоинт.

#### Admin UI (`admin_ui/`)

- FastAPI + Jinja2 веб-интерфейс.
- Страницы:
  - `/` — дашборд статуса;
  - `/search` — тестовый семантический поиск;
  - `/chunks` — просмотр чанков с фильтрацией.
- API:
  - `POST /api/reindex` — запуск переиндексации;
  - `GET /api/search?q=...&doc_type=...&n=...` — тестовый поиск.
- Аутентификация по `ADMIN_API_TOKEN` (header `X-Admin-Token` или query-параметр `token`).

### 2.3. Сетевое взаимодействие

Все сервисы подключены к общей Docker-сети `rag-network`. Внешние порты:

| Сервис | Внутренний порт | Порт на хосте | Примечание |
|--------|-----------------|---------------|------------|
| ChromaDB | 8000 | 8000 | Доступен в локальной сети |
| Indexer | 8001 | — | Только внутри сети Docker |
| Admin UI | 8080 | 8080 | Веб-интерфейс администратора |
| MCP Server | 3000 | 8002 | Для подключения Kimi Code |

---

## 3. Конфигурация

### 3.1. Переменные окружения (`.env`)

Копируйте `.env.example` в `.env` и заполните:

```bash
cp .env.example .env
```

#### ChromaDB

| Переменная | Значение по умолчанию | Описание |
|------------|----------------------|----------|
| `CHROMA_HOST` | `chromadb` | Хост ChromaDB (внутри Docker) |
| `CHROMA_PORT` | `8000` | Порт ChromaDB |
| `CHROMA_TOKEN` | `change-me-to-a-secure-token` | Bearer-токен для доступа к ChromaDB |

#### Indexer

| Переменная | Значение по умолчанию | Описание |
|------------|----------------------|----------|
| `GIT_REPO_URL` | — | URL Git-репозитория с документацией и кодом |
| `GIT_BRANCH` | `main` | Ветка репозитория |
| `GIT_SOURCES_DIR` | `/data/git-sources` | Путь к клону внутри контейнера |
| `SENTENCE_TRANSFORMER_MODEL` | `all-MiniLM-L6-v2` | Модель эмбеддингов |
| `CHROMA_COLLECTION` | `lang_docs` | Имя коллекции в ChromaDB |
| `EMBEDDING_DIMENSION` | `384` | Размерность векторов |
| `INDEXER_LOG_LEVEL` | `INFO` | Уровень логирования |

#### Admin UI

| Переменная | Значение по умолчанию | Описание |
|------------|----------------------|----------|
| `ADMIN_API_TOKEN` | `change-me-to-a-secure-admin-token` | Токен доступа к Admin UI |
| `ADMIN_UI_HOST` | `0.0.0.0` | Хост привязки |
| `ADMIN_UI_PORT` | `8080` | Порт Admin UI |

#### MCP Server

| Переменная | Значение по умолчанию | Описание |
|------------|----------------------|----------|
| `MCP_PORT` | `8002` | Порт MCP на хосте |
| `MCP_AUTH_TOKEN` | `change-me-to-a-secure-mcp-token` | Bearer-токен для MCP-клиентов |
| `MCP_LOG_LEVEL` | `info` | Уровень логирования |

### 3.2. Project-level конфигурация Kimi Code

Для автоматического подключения MCP при открытии проекта создайте файл `/Users/lipanovav/rag/.kimi/mcp.json`:

```json
{
  "mcpServers": {
    "chroma-rag": {
      "url": "http://localhost:8002/mcp",
      "headers": {
        "Authorization": "Bearer <MCP_AUTH_TOKEN>"
      }
    }
  }
}
```

> **Важно:** файл `.kimi/mcp.json` уже добавлен в `.gitignore`, чтобы токен не попал в репозиторий.

### 3.3. Глобальная конфигурация Kimi Code

Альтернативно можно настроить MCP в глобальном конфиге:

```bash
kimi mcp add --transport http chroma-rag http://<host>:8002/mcp \
  --header "Authorization: Bearer <MCP_AUTH_TOKEN>"
```

---

## 4. Требования к инфраструктуре

### 4.1. Локальная разработка

- macOS / Linux / Windows с WSL2;
- Docker Desktop или Docker Engine + Docker Compose;
- ~6 ГБ RAM (4 ГБ под ChromaDB + остальные сервисы);
- ~2 ГБ диска под образы и volume.

### 4.2. Сервер для команды

- Ubuntu LTS / Debian / CentOS;
- Docker + Docker Compose Plugin;
- 8+ ГБ RAM;
- SSD-диск для хранения индекса;
- Доступ к Git-репозиторию с исходниками;
- Сетевой доступ разработчиков к портам 8002 (MCP) и 8080 (Admin UI).

---

## 5. Развёртывание

### 5.1. Локальный запуск

```bash
cd /Users/lipanovav/rag
cp .env.example .env
# отредактируй .env
docker compose up --build
```

Для фонового режима:

```bash
docker compose up --build -d
```

### 5.2. Проверка после запуска

```bash
# ChromaDB
curl http://localhost:8000/api/v1/heartbeat

# MCP Server
curl http://localhost:8002/health

# Admin UI
open http://localhost:8080?token=<ADMIN_API_TOKEN>

# Indexer
curl http://localhost:8001/health
```

### 5.3. Остановка

```bash
docker compose down
```

Остановка с удалением volumes (данные ChromaDB будут потеряны):

```bash
docker compose down -v
```

### 5.4. Автозапуск на macOS

Для автоматического запуска RAG при включении компьютера настроен LaunchAgent:

- Скрипт: `/Users/lipanovav/rag/.kimi/start-rag.sh`
- Конфиг: `~/Library/LaunchAgents/com.rag.docker-compose.plist`

Загрузка агента:

```bash
launchctl load ~/Library/LaunchAgents/com.rag.docker-compose.plist
```

Проверка статуса:

```bash
launchctl list | grep com.rag.docker-compose
```

> **Примечание:** Docker Desktop должен быть настроен на автозапуск при входе в систему. Скрипт `start-rag.sh` ожидает доступности Docker daemon до выполнения `docker compose up -d`.

### 5.5. Production рекомендации

1. **Токены:** замените все плейсхолдеры (`change-me-to-*`) на криптографически стойкие случайные строки (минимум 32 символа).
2. **Сеть:** не выставляйте порты 8000 и 8001 наружу. Достаточно открыть только 8002 (MCP) и 8080 (Admin UI) в локальной сети.
3. **HTTPS:** для удалённого доступа настройте reverse proxy (nginx/traefik) с TLS.
4. **Бэкапы:** регулярно копируйте Docker volume `chroma-data`:
   ```bash
   docker run --rm -v rag_chroma-data:/data -v $(pwd):/backup alpine tar czf /backup/chroma-backup.tar.gz -C /data .
   ```
5. **Мониторинг:** настройте сбор логов контейнеров (`docker compose logs -f`).
6. **Git-доступ:** используйте deploy-token или SSH-ключ для клонирования приватного репозитория.

---

## 6. Подключение

### 6.1. Подключение Kimi Code

#### Вариант A: project-level конфиг (рекомендуется)

Файл `.kimi/mcp.json` в корне проекта подхватывается автоматически при старте сессии.

#### Вариант B: глобальная команда

```bash
kimi mcp add --transport http chroma-rag http://localhost:8002/mcp \
  --header "Authorization: Bearer <MCP_AUTH_TOKEN>"
```

#### Проверка

После подключения в сессии Kimi Code становятся доступны инструменты:

- `search_docs(query, doc_type, n_results)`
- `search_api_reference(query, n_results)`
- `get_example_code(query, n_results)`

### 6.2. Подключение Admin UI

Откройте в браузере:

```
http://localhost:8080?token=<ADMIN_API_TOKEN>
```

Или передайте токен в заголовке:

```bash
curl -H "X-Admin-Token: <ADMIN_API_TOKEN>" http://localhost:8080/api/search?q=test
```

### 6.3. Прямое обращение к ChromaDB

```bash
curl http://localhost:8000/api/v1/collections \
  -H "Authorization: Bearer <CHROMA_TOKEN>"
```

### 6.4. Ручная проверка MCP-протокола

Получение `Mcp-Session-Id`:

```bash
SESSION_ID=$(curl -s -D - http://localhost:8002/mcp \
  -H "Authorization: Bearer <MCP_AUTH_TOKEN>" \
  -H "Accept: text/event-stream" | grep -i mcp-session-id | awk '{print $2}' | tr -d '\r')
```

Инициализация сессии:

```bash
curl http://localhost:8002/mcp \
  -H "Authorization: Bearer <MCP_AUTH_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}'
```

Список инструментов:

```bash
curl http://localhost:8002/mcp \
  -H "Authorization: Bearer <MCP_AUTH_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
```

---

## 7. Безопасность

| Компонент | Механизм | Где хранится |
|-----------|----------|--------------|
| ChromaDB | Bearer token | `CHROMA_TOKEN` в `.env` |
| MCP Server | Bearer token | `MCP_AUTH_TOKEN` в `.env` и `.kimi/mcp.json` |
| Admin UI | Static token | `ADMIN_API_TOKEN` в `.env` |
| Git | Deploy token / SSH key | В `.env` или Docker secrets |

### Рекомендации

- `.env` и `.kimi/mcp.json` не коммитятся в Git (уже в `.gitignore`).
- Для production используйте Docker secrets или внешнее хранилище секретов.
- Разработчикам выдавайте только MCP-токен, не Admin-токен.
- Ограничьте сетевой доступ к ChromaDB (порт 8000) только внутренней сетью Docker.

---

## 8. Мониторинг и проверка работоспособности

### 8.1. Статус контейнеров

```bash
docker compose ps
```

### 8.2. Логи

```bash
# Все сервисы
docker compose logs -f

# Конкретный сервис
docker compose logs -f mcp-server
```

### 8.3. Проверка MCP-инструментов

В сессии Kimi Code выполните запрос, например:

```
Найди в RAG секретный код проекта
```

Если инструменты подключены, Kimi Code вызовет `search_docs` и вернёт результат.

### 8.4. Проверка индекса

В Admin UI на дашборде отображается:
- статус ChromaDB (heartbeat);
- количество чанков в коллекции;
- дата последней индексации;
- версия Git-коммита.

---

## 9. Устранение неполадок

### 9.1. MCP не подключается

1. Проверьте, что контейнер `rag_mcp_server` запущен:
   ```bash
   docker compose ps
   ```
2. Проверьте healthcheck:
   ```bash
   curl http://localhost:8002/health
   ```
3. Проверьте токен в `.kimi/mcp.json` или глобальной конфигурации.
4. Посмотрите логи:
   ```bash
   docker compose logs mcp-server
   ```

### 9.2. Поиск не возвращает результаты

1. Проверьте, что коллекция `lang_docs` не пуста:
   ```bash
   curl http://localhost:8000/api/v1/collections/lang_docs/count \
     -H "Authorization: Bearer <CHROMA_TOKEN>"
   ```
2. Запустите переиндексацию через Admin UI или напрямую:
   ```bash
   curl -X POST http://localhost:8001/reindex
   ```
3. Проверьте `GIT_REPO_URL` и доступность репозитория.

### 9.3. ChromaDB недоступна

1. Проверьте heartbeat:
   ```bash
   curl http://localhost:8000/api/v1/heartbeat
   ```
2. Убедитесь, что `CHROMA_TOKEN` совпадает в `.env` и в запросах.
3. Проверьте логи:
   ```bash
   docker compose logs chromadb
   ```

### 9.4. Admin UI не открывается

1. Проверьте токен в URL или заголовке.
2. Убедитесь, что контейнер `rag_admin_ui` запущен.
3. Проверьте логи:
   ```bash
   docker compose logs admin-ui
   ```

---

## 10. Обновление системы

### 10.1. Обновление кода сервисов

```bash
cd /Users/lipanovav/rag
git pull
docker compose down
docker compose up --build -d
```

### 10.2. Обновление индекса

Через Admin UI нажмите «Pull & Reindex» или выполните:

```bash
curl -X POST http://localhost:8001/reindex
```

### 10.3. Обновление ChromaDB

Перед обновлением образа ChromaDB сделайте бэкап volume:

```bash
docker run --rm -v rag_chroma-data:/data -v $(pwd):/backup alpine \
  tar czf /backup/chroma-backup-$(date +%Y%m%d).tar.gz -C /data .
```

---

## 11. Файлы конфигурации

| Файл | Назначение |
|------|------------|
| `.env` | Переменные окружения и секреты |
| `.env.example` | Шаблон `.env` |
| `docker-compose.yml` | Описание сервисов Docker Compose |
| `.kimi/mcp.json` | Project-level конфиг Kimi Code |
| `~/Library/LaunchAgents/com.rag.docker-compose.plist` | Автозапуск на macOS |
| `.kimi/start-rag.sh` | Скрипт запуска для LaunchAgent |

---

## 12. Сводка endpoint'ов

| Сервис | Endpoint | Метод | Описание |
|--------|----------|-------|----------|
| ChromaDB | `/api/v1/heartbeat` | GET | Проверка доступности |
| ChromaDB | `/api/v1/collections` | GET | Список коллекций |
| Indexer | `/health` | GET | Healthcheck |
| Indexer | `/reindex` | POST | Запуск индексации |
| Admin UI | `/` | GET | Дашборд |
| Admin UI | `/api/reindex` | POST | Запуск переиндексации |
| Admin UI | `/api/search` | GET | Тестовый поиск |
| MCP Server | `/health` | GET | Healthcheck |
| MCP Server | `/mcp` | POST | MCP-протокол |
