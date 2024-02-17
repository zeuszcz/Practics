from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select
from sqlalchemy import text
from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


postgresql_url = 'postgresql://postgres:qw221057320@localhost:3110/postgres'

# engine = create_engine(postgresql_url)
#
# session = sessionmaker(bind=engine)


engine = create_async_engine(postgresql_url)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session








