from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    chroma_host: str = "chromadb"
    chroma_port: int = 8000
    chroma_token: str = ""
    chroma_collection: str = "lang_docs"

    admin_ui_host: str = "0.0.0.0"
    admin_ui_port: int = 8080
    admin_api_token: str = ""
    indexer_api_url: str = "http://indexer:8001"

    sentence_transformer_model: str = "all-MiniLM-L6-v2"
    model_cache_dir: str = "/models"


settings = Settings()
