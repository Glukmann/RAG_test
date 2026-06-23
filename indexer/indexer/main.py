import argparse
import time
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

from indexer.config import settings
from indexer.logger import logger
from indexer.git_client import ensure_repo
from indexer.chunker import chunk_document, SUPPORTED_EXTS
from indexer.embeddings import embed
from indexer.chroma_client import get_client, get_collection, upsert_chunks

app = FastAPI(title="RAG Indexer API")


def collect_files(repo_dir: Path) -> list[Path]:
    files: list[Path] = []
    for ext in SUPPORTED_EXTS:
        files.extend(repo_dir.rglob(f"*{ext}"))
    return files


def run_indexing() -> dict:
    logger.info("Starting indexing...")
    start = time.time()

    repo_dir, commit_hash = ensure_repo()
    files = collect_files(repo_dir)
    logger.info("Found %d files to process", len(files))

    all_chunks: list[dict] = []
    errors: list[str] = []
    for file in files:
        try:
            chunks = chunk_document(file)
            all_chunks.extend(chunks)
        except Exception as exc:
            msg = f"Failed to process {file}: {exc}"
            logger.error(msg)
            errors.append(msg)

    logger.info("Total chunks: %d", len(all_chunks))

    if all_chunks:
        texts = [c["text"] for c in all_chunks]
        logger.info("Computing embeddings with model %s...", settings.sentence_transformer_model)
        embeddings = embed(texts)

        logger.info("Storing %d chunks in ChromaDB...", len(all_chunks))
        client = get_client()
        collection = get_collection(client)
        upsert_chunks(collection, all_chunks, embeddings, commit_hash)

    duration = time.time() - start
    logger.info("Indexing complete in %.2f seconds", duration)

    return {
        "status": "success" if not errors else "partial",
        "commit_hash": commit_hash,
        "files_processed": len(files),
        "chunks_indexed": len(all_chunks),
        "errors": errors,
        "duration_seconds": round(duration, 2),
    }


@app.post("/reindex")
def reindex():
    result = run_indexing()
    return JSONResponse(content=result)


@app.get("/health")
def health():
    return {"status": "ok"}


def main():
    parser = argparse.ArgumentParser(description="RAG Indexer")
    parser.add_argument("command", choices=["run", "api"], help="run: single indexing pass; api: start HTTP API")
    args = parser.parse_args()

    if args.command == "run":
        result = run_indexing()
        print(result)
    elif args.command == "api":
        uvicorn.run(app, host=settings.indexer_api_host, port=settings.indexer_api_port)


if __name__ == "__main__":
    main()
