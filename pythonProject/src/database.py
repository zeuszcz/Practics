from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select
from sqlalchemy import text
from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


postgresql_url = 'postgresql://postgres:qw221057320@localhost:3110/postgres'

engine = create_engine(postgresql_url)
Session = sessionmaker(bind=engine)





def get_session():
    with Session() as session:
        yield session








