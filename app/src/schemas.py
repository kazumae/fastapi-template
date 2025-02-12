from datetime import datetime

from pydantic import BaseModel


class TestBase(BaseModel):
    name: str
    description: str | None = None


class TestCreate(TestBase):
    pass


class Test(TestBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
