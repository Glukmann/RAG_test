from typing import Any

import chromadb
from chromadb.config import Settings as ChromaSettings
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

from mcp_gateway.config import settings

_client: chromadb.ClientAPI | None = None
_collection: Any = None
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


def get_collection():
    global _collection
    if _collection is None:
        _collection = get_client().get_or_create_collection(
            name=settings.chroma_collection,
            metadata={"hnsw:space": "cosine"},
        )
    return _collection


def get_model() -> Any:
    global _model
    if _model is None:
        _model = DefaultEmbeddingFunction()
    return _model


def query_collection(query: str, n_results: int = 5, where: dict | None = None):
    model = get_model()
    embedding = model([query])
    collection = get_collection()
    return collection.query(
        query_embeddings=embedding,
        n_results=n_results,
        where=where,
        include=["documents", "metadatas", "distances"],
    )
