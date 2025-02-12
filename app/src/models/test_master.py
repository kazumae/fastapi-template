from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database import Base


class TestMaster(Base):
    __tablename__ = "test_masters"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # リレーションシップの定義
    tests = relationship("Test", back_populates="test_master")
