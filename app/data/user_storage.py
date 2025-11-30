from typing import List
from app.models.user_model import User

# Temporary in-memory data store
users: List[User] = []

# Auto-increment ID counter
next_id = 1
