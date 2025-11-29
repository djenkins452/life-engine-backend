from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.auth.hashing import Hasher
from app.auth.jwt_handler import create_access_token
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])

# Request Models
class RegisterRequest(BaseModel):
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/register")
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already exists.")

    hashed_pw = Hasher.hash_password(request.password)
    new_user = User(email=request.email, password_hash=hashed_pw)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully", "user_id": new_user.id}


@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials.")

    if not Hasher.verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials.")

    token = create_access_token({"sub": user.email})

    return {"access_token": token, "token_type": "bearer"}


# Protected route
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

from jose import jwt, JWTError
from app.auth.jwt_handler import SECRET_KEY, ALGORITHM

@router.get("/me")
def get_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        user = db.query(User).filter(User.email == email).first()
        return {"id": user.id, "email": user.email}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

