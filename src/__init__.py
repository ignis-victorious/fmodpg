#
#  _________________
#  Import LIBRARIES
from fastapi import FastAPI
from contextlib import asynccontextmanager

#  Import FILES
from src.db.main import init_db
#  _________________


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is starting")
    await init_db()

    yield
    print("server is shutting down")


app = FastAPI(
    title="Book service",
    version="0.1.0",
    description="A simple example of how to runa FastAPI application that access both endpoints and a Postgres database",
    # docs_url="/",
    # redoc_url="/",
    # openapi_url="/openapi.json",
    lifespan=lifespan,
)


@app.get("/ping")
async def ping() -> dict[str, str]:
    return {"message": "pong"}
