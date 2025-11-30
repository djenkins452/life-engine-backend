from fastapi import APIRouter
from app.models.user_model import User
from app.data.user_storage import users, next_id

router = APIRouter()

@router.post("/users")
def create_user(name: str, email: str, age: int):
    global next_id

    new_user = User(
        id=next_id,
        name=name,
        email=email,
        age=age
    )
    users.append(new_user)
    next_id += 1

    return {"message": "user created", "user": new_user}

@router.get("/users")
def get_all_users():
    return users

@router.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "user not found"}
