from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    chroma_host: str = "chromadb"
    chroma_port: int = 8000
    chroma_token: str = ""
    chroma_collection: str = "lang_docs"

    sentence_transformer_model: str = "all-MiniLM-L6-v2"
    model_cache_dir: str = "/models"

    mcp_log_level: str = "INFO"


settings = Settings()
