from fastapi import FastAPI

from app.database import Base, engine
from app import models

from app.routers import health
from app.auth.routes import router as auth_router

# Important: Create database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Life Engine API", version="0.1.0")

# Routers
app.include_router(health.router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Life Engine API running"}
