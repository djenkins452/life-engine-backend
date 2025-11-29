from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.auth.hashing import Hasher
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterRequest(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/register")
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    # Check if email already exists
    existing = db.query(User).filter(User.email == request.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = Hasher.hash_password(request.password)

    new_user = User(email=request.email, password_hash=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created", "user_id": new_user.id}


@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not Hasher.verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {"message": "Login successful", "user_id": user.id}
