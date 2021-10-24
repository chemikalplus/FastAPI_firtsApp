from fastapi import FastAPI
from core.config import setting
from db.session import engine
from db.base_class import Base

def createTables():
    Base.metadata.create_all(bind=engine)

def startApp():
    app = FastAPI(title=setting.PROJECT_TITLE, version=setting.PROJECT_VERSION)
    createTables()
    return app


app = startApp()

@app.get("/")
def main():
    return {"saludo" : "Hola"}



