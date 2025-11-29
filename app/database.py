from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Get database URL from Render environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# IMPORTANT: Base class for all models
Base = declarative_base()


# Dependency injected into routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
