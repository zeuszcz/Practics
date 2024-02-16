from psycopg2._psycopg import connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select
from sqlalchemy import text

postgresql_url = 'postgresql://postgres:qw221057320@localhost:3110/postgres'

engine = create_engine(postgresql_url)
with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(res)
Session = sessionmaker(bind=engine)










