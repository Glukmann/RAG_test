import logging
import sys

from mcp.server.auth.provider import AccessToken, TokenVerifier
from mcp.server.auth.settings import AuthSettings
from mcp.server.fastmcp import FastMCP
from pydantic import AnyHttpUrl
from starlette.requests import Request
from starlette.responses import JSONResponse
import uvicorn

from mcp_server.config import settings
from mcp_server import tools as rag_tools

logging.basicConfig(
    level=getattr(logging, settings.mcp_log_level.upper(), logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stderr)],
)
logger = logging.getLogger("mcp_server")


class StaticTokenVerifier(TokenVerifier):
    """Простая проверка единого Bearer-токена."""

    async def verify_token(self, token: str) -> AccessToken | None:
        if token != settings.mcp_auth_token:
            return None
        return AccessToken(
            token=token,
            client_id="rag-client",
            scopes=["mcp"],
        )


mcp = FastMCP(
    "rag-mcp-server",
    host=settings.mcp_host,
    port=settings.mcp_port,
    token_verifier=StaticTokenVerifier(),
    auth=AuthSettings(
        issuer_url=AnyHttpUrl("http://localhost"),
        resource_server_url=AnyHttpUrl("http://localhost"),
    ),
)


@mcp.tool()
async def search_docs(query: str, doc_type: str | None = None, n_results: int = 5) -> dict:
    """Semantic search over documentation and code collection."""
    return rag_tools.search_docs(query, doc_type=doc_type, n_results=n_results)


@mcp.tool()
async def search_api_reference(query: str, n_results: int = 5) -> dict:
    """Search for function/type definitions, prioritizing code examples."""
    return rag_tools.search_api_reference(query, n_results=n_results)


@mcp.tool()
async def get_example_code(query: str, n_results: int = 5) -> dict:
    """Find code examples for a given topic or function."""
    return rag_tools.get_example_code(query, n_results=n_results)


@mcp.custom_route("/health", methods=["GET"])
async def health(request: Request):
    return JSONResponse({"status": "ok"})


def main():
    logger.info("Starting RAG MCP server on %s:%s", settings.mcp_host, settings.mcp_port)
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
