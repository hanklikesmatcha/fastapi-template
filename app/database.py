import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


if os.environ.get("PWD") == "/Users/hank/src/hank/backend":
    SQLALCHEMY_DATABASE_URL = "postgresql://admin:password@localhost:5431/backend_db"
else:
    SQLALCHEMY_DATABASE_URL = (
        "postgresql://admin:password@postgres-server:5432/backend_db"
    )

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def db_connection():
    session = Session()
    try:
        yield session
    finally:
        session.close()
