from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

SYNC_URL = "postgresql+psycopg2://user:password@localhost:5432/benchmark"
ASYNC_URL = "postgresql+asyncpg://user:password@localhost:5432/benchmark"

SYNC_ENGINE = create_engine(SYNC_URL)
ASYNC_ENGINE = create_async_engine(ASYNC_URL)

SYNC_SESSION = sessionmaker(bind=SYNC_ENGINE, expire_on_commit=False)
ASYNC_SESSION = async_sessionmaker(bind=ASYNC_ENGINE, expire_on_commit=False)
