from fastapi import FastAPI
from app.database import Base, engine
from app.auth.routes import router as auth_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Life Engine API")

# Health check
@app.get("/health/")
def health_check():
    return {"status": "ok"}

# Mount auth router
app.include_router(auth_router, prefix="/auth", tags=["auth"])
