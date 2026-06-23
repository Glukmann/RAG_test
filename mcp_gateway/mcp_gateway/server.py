import asyncio
import json
import logging
import sys

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from mcp_gateway.config import settings
from mcp_gateway import tools as rag_tools

logging.basicConfig(
    level=getattr(logging, settings.mcp_log_level.upper(), logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stderr)],
)
logger = logging.getLogger("mcp_gateway")

app = Server("rag-mcp-gateway")

SEARCH_DOCS_SCHEMA = {
    "type": "object",
    "properties": {
        "query": {"type": "string", "description": "Search query in natural language"},
        "doc_type": {
            "type": "string",
            "enum": ["docs", "code_examples"],
            "description": "Optional filter by document type",
        },
        "n_results": {
            "type": "integer",
            "default": 5,
            "description": "Number of results to return",
        },
    },
    "required": ["query"],
}

SEARCH_API_SCHEMA = {
    "type": "object",
    "properties": {
        "query": {"type": "string", "description": "Function or type name to search"},
        "n_results": {"type": "integer", "default": 5},
    },
    "required": ["query"],
}

EXAMPLE_CODE_SCHEMA = {
    "type": "object",
    "properties": {
        "query": {"type": "string", "description": "Topic or function to find examples for"},
        "n_results": {"type": "integer", "default": 5},
    },
    "required": ["query"],
}


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search_docs",
            description="Semantic search over documentation and code collection.",
            inputSchema=SEARCH_DOCS_SCHEMA,
        ),
        Tool(
            name="search_api_reference",
            description="Search for function/type definitions, prioritizing code examples.",
            inputSchema=SEARCH_API_SCHEMA,
        ),
        Tool(
            name="get_example_code",
            description="Find code examples for a given topic or function.",
            inputSchema=EXAMPLE_CODE_SCHEMA,
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    logger.debug("Tool call: %s(%s)", name, arguments)
    query = arguments.get("query", "")
    n_results = arguments.get("n_results", 5)

    if name == "search_docs":
        doc_type = arguments.get("doc_type")
        results = rag_tools.search_docs(query, doc_type=doc_type, n_results=n_results)
    elif name == "search_api_reference":
        results = rag_tools.search_api_reference(query, n_results=n_results)
    elif name == "get_example_code":
        results = rag_tools.get_example_code(query, n_results=n_results)
    else:
        raise ValueError(f"Unknown tool: {name}")

    text = json.dumps(results, ensure_ascii=False, indent=2)
    return [TextContent(type="text", text=text)]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options(),
        )


if __name__ == "__main__":
    asyncio.run(main())
