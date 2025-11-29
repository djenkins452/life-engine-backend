from fastapi import FastAPI
from app.routers import health

app = FastAPI(title="Life Engine API")

app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Life Engine API is running!"}
