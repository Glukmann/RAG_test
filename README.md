# RAG на базе ChromaDB

Система централизованной векторной базы знаний для команды разработчиков.

## Компоненты

1. **ChromaDB Server** — векторная база данных с HTTP API и Bearer token аутентификацией.
2. **Indexer** — сервис индексации документации и примеров кода из Git-репозитория.
3. **MCP Gateway** — read-only MCP-шлюз для интеграции с Kimi Code.
4. **Admin UI** — веб-интерфейс для мониторинга и управления индексацией.

## Быстрый старт

```bash
cp .env.example .env
# отредактируй .env: укажи GIT_REPO_URL, CHROMA_TOKEN, ADMIN_API_TOKEN
docker compose up --build
```

- ChromaDB API: http://localhost:8000
- Admin UI: http://localhost:8080

## Документация

- Техническое задание: [RAG_ChromaDB_TZ.md](./RAG_ChromaDB_TZ.md)
- Инструкции для агентов: [AGENTS.md](./AGENTS.md)
