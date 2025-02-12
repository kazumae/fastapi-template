from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .... import crud
from ....schemas import test as schemas
from ....schemas.common import ListResponse
from ...deps import get_db

router = APIRouter()


@router.get("/", response_model=ListResponse[schemas.Test])
def read_tests(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> ListResponse[schemas.Test]:
    tests, total = crud.crud_test.get_tests(db, skip=skip, limit=limit)
    return ListResponse(
        paginate={"total": total, "skip": skip, "limit": limit},
        items=tests,
    )


@router.get("/{test_id}", response_model=schemas.Test)
def read_test(test_id: int, db: Session = Depends(get_db)) -> schemas.Test:
    test = crud.crud_test.get_test(db, test_id=test_id)
    if test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return test


@router.post("/", response_model=schemas.Test)
def create_test(
    test: schemas.TestCreate, db: Session = Depends(get_db)
) -> schemas.Test:
    return crud.crud_test.create_test(db=db, test=test)
