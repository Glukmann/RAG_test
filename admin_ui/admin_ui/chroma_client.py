from typing import Any

import chromadb
from chromadb.config import Settings as ChromaSettings
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

from admin_ui.config import settings

_client: chromadb.ClientAPI | None = None
_model: Any = None


def get_client() -> chromadb.ClientAPI:
    global _client
    if _client is None:
        _client = chromadb.HttpClient(
            host=settings.chroma_host,
            port=settings.chroma_port,
            settings=ChromaSettings(
                chroma_client_auth_provider="chromadb.auth.token_authn.TokenAuthClientProvider",
                chroma_client_auth_credentials=settings.chroma_token,
            ),
        )
    return _client


def get_model() -> Any:
    global _model
    if _model is None:
        _model = DefaultEmbeddingFunction()
    return _model


def heartbeat() -> bool:
    try:
        client = get_client()
        client.heartbeat()
        return True
    except Exception:
        return False


def get_collection_count() -> int | None:
    try:
        collection = get_client().get_collection(settings.chroma_collection)
        return collection.count()
    except Exception:
        return None


def list_collections() -> list[str]:
    try:
        # ChromaDB >= 0.6.0 returns list of collection names (strings)
        collections = get_client().list_collections()
        if collections and isinstance(collections[0], str):
            return collections
        # Fallback for older ChromaDB versions returning collection objects
        return [c.name for c in collections]
    except Exception:
        return []


def query_collection(query: str, n_results: int = 5, where: dict | None = None):
    model = get_model()
    embedding = model([query])
    collection = get_client().get_collection(settings.chroma_collection)
    return collection.query(
        query_embeddings=embedding,
        n_results=n_results,
        where=where,
        include=["documents", "metadatas", "distances"],
    )


def get_chunks(skip: int = 0, limit: int = 20, where: dict | None = None):
    collection = get_client().get_collection(settings.chroma_collection)
    return collection.get(
        where=where,
        limit=limit,
        offset=skip,
        include=["documents", "metadatas"],
    )


def get_collection_info(name: str) -> dict | None:
    try:
        collection = get_client().get_collection(name)
        return {
            "name": name,
            "count": collection.count(),
        }
    except Exception:
        return None


def clear_collection(name: str) -> int:
    collection = get_client().get_collection(name)
    all_ids = collection.get(include=[])["ids"]
    if all_ids:
        collection.delete(ids=all_ids)
    return len(all_ids)


def delete_collection(name: str) -> bool:
    get_client().delete_collection(name)
    return True
