from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Git
    git_repo_url: str = ""
    git_branch: str = "main"
    git_sources_dir: str = "/data/git-sources"

    # Embeddings
    sentence_transformer_model: str = "all-MiniLM-L6-v2"
    embedding_dimension: int = 384
    model_cache_dir: str = "/models"

    # ChromaDB
    chroma_host: str = "chromadb"
    chroma_port: int = 8000
    chroma_token: str = ""
    chroma_collection: str = "lang_docs"

    # Indexer API
    indexer_api_host: str = "0.0.0.0"
    indexer_api_port: int = 8001
    indexer_log_level: str = "INFO"


settings = Settings()
