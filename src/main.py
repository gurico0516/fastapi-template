from fastapi import FastAPI
from src.logging.logging_config import setup_logging


setup_logging()

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}
