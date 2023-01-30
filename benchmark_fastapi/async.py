from typing import AsyncIterator, Sequence
from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn

from benchmark_fastapi import db, models, schemas


async def get_db() -> AsyncIterator[AsyncSession]:
    async with db.ASYNC_SESSION() as session:
        yield session


app = FastAPI()


@app.get("/users", response_model=list[schemas.User])
async def get_users(db: AsyncSession = Depends(get_db)) -> Sequence[models.User]:
    stmt = select(models.User)
    db_users = (await db.scalars(stmt)).unique().all()
    return db_users


@app.post("/users", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate, db: AsyncSession = Depends(get_db)
) -> models.User:
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000)
