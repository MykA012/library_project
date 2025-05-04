from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from config import load_settings


# DATABASE_URL = f"postgresql+psycopg2://postgres:postgres@localhost:5432/sa"

engine = create_engine(load_settings().db_url)

session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Session:
    with session_maker() as session:
        yield session

class Base(DeclarativeBase):
    pass