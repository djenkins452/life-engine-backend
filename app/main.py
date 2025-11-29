from fastapi import FastAPI
from app.routers import health
from app.auth.routes import router as auth_router

app = FastAPI(title="Life Engine API")

app.include_router(health.router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Life Engine API is running!"}
