from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Add models later (User, Glucose, Fasting, Weight, etc.)

from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
