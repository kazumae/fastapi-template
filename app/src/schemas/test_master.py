from datetime import datetime

from pydantic import BaseModel


class TestMasterBase(BaseModel):
    code: str
    name: str
    description: str | None = None


class TestMaster(TestMasterBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
