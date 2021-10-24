import os
from pathlib import Path
from dotenv import load_dotenv

envPath = Path('.') / '.env'
load_dotenv(dotenv_path=envPath)


class Setting:
    PROJECT_TITLE: str = "Josem's FastAPI"
    PROJECT_VERSION:str = "0.1.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD : str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "fastAPIApp1")
    DATABASE_URL : str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

setting = Setting()
