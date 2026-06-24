# RAG на базе ChromaDB

Система централизованной векторной базы знаний для команды разработчиков.

## Компоненты

1. **ChromaDB Server** — векторная база данных с HTTP API и Bearer token аутентификацией.
2. **Indexer** — сервис индексации документации и примеров кода из Git-репозитория.
3. **MCP Server** — собственный HTTP MCP-сервер для интеграции с Kimi Code. Предоставляет инструменты поиска по ChromaDB через единый Bearer-токен.
4. **Admin UI** — веб-интерфейс для мониторинга и управления индексацией.

## Быстрый старт

```bash
cp .env.example .env
# отредактируй .env: укажи GIT_REPO_URL, CHROMA_TOKEN, ADMIN_API_TOKEN, MCP_AUTH_TOKEN
docker compose up --build
```

- ChromaDB API: http://localhost:8000
- Admin UI: http://localhost:8080
- MCP Server: http://localhost:8002/mcp

## Подключение Kimi Code

```bash
kimi mcp add --transport http chroma-rag http://<host>:8002/mcp \
  --header "Authorization: Bearer <MCP_AUTH_TOKEN>"
```

где `<host>` — IP или hostname сервера в локальной сети, `<MCP_AUTH_TOKEN>` — значение из `.env`.

Каждый разработчик использует один и тот же URL и токен. MCP-сервер stateless, поэтому несколько клиентов Kimi Code могут подключаться одновременно.

## Проверка работы

После запуска убедись, что MCP-сервер отвечает:

```bash
curl http://localhost:8002/health
```

Проверь авторизацию и протокол (streamable HTTP). Сначала получи `Mcp-Session-Id` из заголовка ответа, затем выполни инициализацию и запроси список инструментов:

```bash
SESSION_ID=$(curl -s -D - http://localhost:8002/mcp \
  -H "Authorization: Bearer <MCP_AUTH_TOKEN>" \
  -H "Accept: text/event-stream" | grep -i mcp-session-id | awk '{print $2}' | tr -d '\r')

curl http://localhost:8002/mcp \
  -H "Authorization: Bearer <MCP_AUTH_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}'

curl http://localhost:8002/mcp \
  -H "Authorization: Bearer <MCP_AUTH_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
```

## Документация

- Архитектура и развёртывание: [ARCHITECTURE_AND_DEPLOYMENT.md](./ARCHITECTURE_AND_DEPLOYMENT.md)
- Инструкции для агентов: [AGENTS.md](./AGENTS.md)
