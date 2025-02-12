from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class PaginateSchema(BaseModel):
    total: int
    skip: int
    limit: int


class ListResponse(BaseModel, Generic[T]):
    paginate: PaginateSchema
    items: list[T]
