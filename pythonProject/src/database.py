from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select
from sqlalchemy import text

postgresql_url = 'postgresql://postgres:1111@localhost:3110/postgres'

engine = create_engine(postgresql_url)

session = sessionmaker(bind=engine)











