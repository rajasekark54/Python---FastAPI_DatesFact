import os
from dotenv import load_dotenv
from pathlib import Path
from core.logger import get_logger

logger = get_logger(__name__)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    logger.info("Loading config settings from the environment...")
    PROJECT_NAME:str = "Dates Fact"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    NUMBERSAPI : str = os.getenv("NUMBERSAPI")

settings = Settings()