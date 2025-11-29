from pydantic import BaseModel, Field, EmailStr

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(
        ...,
        min_length=6,
        max_length=72,
        description="Password must be between 6 and 72 characters because bcrypt cannot hash more than 72 bytes."
    )

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(
        ...,
        min_length=1,
        description="User's password"
    )

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
