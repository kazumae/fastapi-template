from fastapi import FastAPI
from minio import Minio

from .api.v1.router import api_router
from .config import settings

app = FastAPI()

# MinIOクライアントの初期化
minio_client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False,
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router, prefix="/api/v1")
