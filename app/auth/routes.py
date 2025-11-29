from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.schemas import RegisterRequest, LoginRequest, TokenResponse
from app.auth.hashing import Hasher
from app.auth.jwt_handler import create_access_token
from app.models import User
from app.database import get_db

router = APIRouter()

@router.get("/health/")
def auth_health():
    return {"status": "auth ok"}

@router.post("/register")
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == request.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_pw = Hasher.hash_password(request.password)
    user = User(email=request.email, password_hash=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User created", "user_id": user.id}

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not Hasher.verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": str(user.id)})
    return TokenResponse(access_token=token)

@router.get("/me")
def me(db: Session = Depends(get_db)):
    return {"message": "me endpoint working"}
