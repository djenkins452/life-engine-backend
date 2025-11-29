from fastapi import FastAPI
from app.routers.metrics import router as metrics_router

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

# MOUNT THE ROUTER (Critical line)
app.include_router(metrics_router, prefix="/api")
