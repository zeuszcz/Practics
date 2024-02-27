from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
from src.config import DB_URL





engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)


def get_session():
    with Session() as session:
        yield session
