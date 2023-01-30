from typing import Generator, Sequence
from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
import uvicorn

from benchmark_fastapi import db, models, schemas


def get_db() -> Generator[Session, None, None]:
    db_session = db.SYNC_SESSION()
    try:
        yield db_session
    finally:
        db_session.close()


app = FastAPI()


@app.get("/users", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)) -> Sequence[models.User]:
    stmt = select(models.User)
    db_users = db.scalars(stmt).unique().all()
    return db_users


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> models.User:
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/addresses", response_model=schemas.Address)
def create_address(
    address: schemas.AddressCreate, db: Session = Depends(get_db)
) -> models.Address:
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000)
