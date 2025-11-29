from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Load DB URL from Render environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine
engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True
)

# SessionLocal is used for dependency injection in routes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the class all models inherit from
Base = declarative_base()


# Dependency used in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
