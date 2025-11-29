from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from app.database import Base


# ----------------------------
# User Model (Authentication)
# ----------------------------

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

    # Future fields (uncomment later)
    # first_name = Column(String, nullable=True)
    # last_name = Column(String, nullable=True)
    # created_at = Column(DateTime, server_default=func.now())


# --------------------------------------------------
# Future expansion models you will add later:
# --------------------------------------------------

# Example for Fasting Sessions
"""
class FastingSession(Base):
    __tablename__ = "fasting_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)
    status = Column(String, nullable=False)  # ongoing / completed / canceled
"""

# Example for Glucose Readings
"""
class GlucoseReading(Base):
    __tablename__ = "glucose_readings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    value = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    source = Column(String, default="manual")  # dexcom / manual
"""

# Example for Weight Tracking
"""
class WeightEntry(Base):
    __tablename__ = "weight_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    weight = Column(Float, nullable=False)
    timestamp = Column(DateTime, server_default=func.now())
"""
