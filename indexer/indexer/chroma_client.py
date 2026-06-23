import chromadb
from chromadb.config import Settings as ChromaSettings

from indexer.config import settings


def get_client() -> chromadb.ClientAPI:
    return chromadb.HttpClient(
        host=settings.chroma_host,
        port=settings.chroma_port,
        settings=ChromaSettings(
            chroma_client_auth_provider="chromadb.auth.token_authn.TokenAuthClientProvider",
            chroma_client_auth_credentials=settings.chroma_token,
        ),
    )


def get_collection(client: chromadb.ClientAPI):
    return client.get_or_create_collection(
        name=settings.chroma_collection,
        metadata={"hnsw:space": "cosine"},
    )


def upsert_chunks(
    collection,
    chunks: list[dict],
    embeddings: list[list[float]],
    version: str,
):
    ids = [f"{chunk['source']}:{i}:{version}" for i, chunk in enumerate(chunks)]
    documents = [chunk["text"] for chunk in chunks]
    metadatas = [
        {
            "source": chunk["source"],
            "doc_type": chunk["doc_type"],
            "language": chunk["language"],
            "chunk_index": i,
            "file_ext": chunk["file_ext"],
            "version": version,
        }
        for i, chunk in enumerate(chunks)
    ]
    collection.upsert(ids=ids, embeddings=embeddings, documents=documents, metadatas=metadatas)
