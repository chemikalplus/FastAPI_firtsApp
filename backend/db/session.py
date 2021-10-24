from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import setting

SQLALQUEMY_DATABASE_URL = setting.DATABASE_URL
engine = create_engine(SQLALQUEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)