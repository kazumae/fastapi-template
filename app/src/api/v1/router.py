from fastapi import APIRouter

from .endpoints import tests

api_router = APIRouter()
api_router.include_router(tests.router, prefix="/tests", tags=["tests"])
