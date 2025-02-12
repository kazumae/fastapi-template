from sqlalchemy.orm import Session

from ..models.test import Test
from ..schemas.test import TestCreate


def get_test(db: Session, test_id: int) -> Test | None:
    return db.query(Test).filter(Test.id == test_id).first()


def get_tests(db: Session, skip: int = 0, limit: int = 100) -> tuple[list[Test], int]:
    query = db.query(Test)
    total = query.count()
    tests = query.offset(skip).limit(limit).all()
    return tests, total


def create_test(db: Session, test: TestCreate) -> Test:
    db_test = Test(**test.model_dump())
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test
