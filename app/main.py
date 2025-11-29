
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Life Engine API - Layer 1 Running"}

@app.get("/health")
def health():
    return {"status": "ok"}
