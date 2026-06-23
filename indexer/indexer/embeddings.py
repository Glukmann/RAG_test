from typing import Any

from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

_model: Any = None


def get_model() -> Any:
    global _model
    if _model is None:
        _model = DefaultEmbeddingFunction()
    return _model


def embed(texts: list[str]) -> list[list[float]]:
    model = get_model()
    embeddings = model(texts)
    return [[float(v) for v in e] for e in embeddings]
