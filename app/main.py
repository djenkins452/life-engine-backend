from fastapi import FastAPI
from app.routers.metrics import router as metrics_router

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(metrics_router, prefix="/api")
