from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str
    MONGODB_DB_NAME: str
    MONGODB_COLLECTION_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()