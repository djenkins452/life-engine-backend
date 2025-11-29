from fastapi import FastAPI
from app.routers import health
from app.auth.routes import router as auth_router
from app.database import Base, engine
from app import models

app = FastAPI(title="Life Engine API")

# Create all tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(health.router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Life Engine API is running!"}
