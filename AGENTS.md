# AGENTS.md — RAG ChromaDB

## Назначение

Монорепозиторий системы RAG на базе ChromaDB с административным интерфейсом и MCP-шлюзом для Kimi Code.

## Структура

- `chroma/` — Dockerfile для ChromaDB Server.
- `indexer/` — сервис индексации (git pull → чанкинг → эмбеддинги → ChromaDB).
- `mcp_server/` — собственный HTTP MCP-сервер для Kimi Code.
- `admin_ui/` — веб-интерфейс администратора.
- `scripts/` — скрипты обработки сырых данных (PDF → MD, чистка, разбиение, извлечение паттернов и примеров).
- `examples/` — примеры использования RSL.
- `ARCHITECTURE_AND_DEPLOYMENT.md` — полное руководство по архитектуре, развёртыванию и интеграции.

## Запуск

```bash
cp .env.example .env
# отредактируй .env
docker compose up --build
```

## Конвенции

- Python 3.12.
- Собственные сервисы (`chroma/`, `indexer/`, `admin_ui/`, `mcp_server/`) живут в своих директориях со своим `Dockerfile` и `requirements.txt`.
- Скрипты обработки данных и генерации знаний живут в `scripts/`.
- Конфигурация через переменные окружения (см. `.env.example`).
- MCP-сервер требует `MCP_AUTH_TOKEN`; Admin UI требует `ADMIN_API_TOKEN`.

## Источники знаний

- Индексатор забирает документацию и код из репозитория `GIT_REPO_URL`, ветки `GIT_BRANCH`, директории `GIT_SOURCES_DIR`.
- Локальная копия источников монтируется в `git-sources/` и игнорируется Git (`.gitignore`).
- Основная коллекция в ChromaDB: `lang_docs`.
- Чанкер определяет `doc_type` по пути/имени файла: `code_examples` для `practice/`, `pattern_`, `example`; иначе `docs`.

## Работа с знаниями через MCP

При ответах на вопросы по RSL/RS-Bank и при написании кода агент должен обращаться к MCP-инструментам `chroma-rag`:

- `search_docs(query, doc_type, n_results)` — семантический поиск по документации.
- `search_api_reference(query, n_results)` — поиск определений функций, классов, процедур.
- `get_example_code(query, n_results)` — поиск примеров кода.

Параметр `doc_type` принимает значения `docs` (документация) или `code_examples` (примеры кода).
