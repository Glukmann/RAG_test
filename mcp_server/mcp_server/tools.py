from mcp_server.chroma_client import query_collection


def search_docs(query: str, doc_type: str | None = None, n_results: int = 5) -> dict:
    where = {"doc_type": doc_type} if doc_type else None
    return query_collection(query, n_results=n_results, where=where)


def search_api_reference(query: str, n_results: int = 5) -> dict:
    return query_collection(
        query,
        n_results=n_results,
        where={"doc_type": "code_examples"},
    )


def get_example_code(query: str, n_results: int = 5) -> dict:
    return query_collection(
        query,
        n_results=n_results,
        where={"doc_type": "code_examples"},
    )
