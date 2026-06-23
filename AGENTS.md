# AGENTS.md — RAG ChromaDB

## Назначение

Монорепозиторий системы RAG на базе ChromaDB с административным интерфейсом и MCP-шлюзом для Kimi Code.

## Структура

- `chroma/` — Dockerfile для ChromaDB Server.
- `indexer/` — сервис индексации (git pull → чанкинг → эмбеддинги → ChromaDB).
- `mcp_server/` — собственный HTTP MCP-сервер для Kimi Code.
- `admin_ui/` — веб-интерфейс администратора.
- `RAG_ChromaDB_TZ.md` — исходное техническое задание.

## Запуск

```bash
cp .env.example .env
# отредактируй .env
docker compose up --build
```

## Конвенции

- Python 3.12.
- Собственные сервисы (`chroma/`, `indexer/`, `admin_ui/`) живут в своих директориях со своим `Dockerfile` и `requirements.txt`. MCP-сервер используется готовый образ `devsaurus/chromadb-remote-mcp`.
- Конфигурация через переменные окружения (см. `.env.example`).
- MCP-сервер требует `MCP_AUTH_TOKEN`; Admin UI требует `ADMIN_API_TOKEN`.
