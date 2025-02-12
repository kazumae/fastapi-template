from fastapi import Depends, FastAPI
from minio import Minio
from sqlalchemy.orm import Session

from . import models
from .config import settings
from .database import get_db

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


@app.get("/tests")
def read_tests(db: Session = Depends(get_db)):
    tests = db.query(models.Test).all()
    return tests
