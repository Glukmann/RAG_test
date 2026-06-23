# AGENTS.md — RAG ChromaDB

## Назначение

Монорепозиторий системы RAG на базе ChromaDB с административным интерфейсом и MCP-шлюзом для Kimi Code.

## Структура

- `chroma/` — Dockerfile для ChromaDB Server.
- `indexer/` — сервис индексации (git pull → чанкинг → эмбеддинги → ChromaDB).
- `mcp_gateway/` — read-only MCP-шлюз для Kimi Code.
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
- Каждый сервис живёт в своей директории со своим `Dockerfile` и `requirements.txt`.
- Конфигурация через переменные окружения (см. `.env.example`).
- Read-only доступ для MCP; Admin UI требует `ADMIN_API_TOKEN`.
