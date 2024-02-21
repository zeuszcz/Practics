from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os

database_url = 'postgresql://postgres:qw221057320@localhost:3110/postgres'



engine = create_engine(database_url)
Session = sessionmaker(bind=engine)


def get_session():
    with Session() as session:
        yield session
