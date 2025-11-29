from fastapi import FastAPI
from app.database import Base, engine
from app.auth.routes import router as auth_router  # <-- FIXED
from fastapi.middleware.cors import CORSMiddleware

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Life Engine API")

# CORS (allow everything for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health/")
def health_check():
    return {"status": "ok"}

# Include AUTH router
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "Life Engine backend running"}
