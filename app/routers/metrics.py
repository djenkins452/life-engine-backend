# app/routers/metrics.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics/basic")
def get_basic_metrics():
    return {
        "steps": 5243,
        "exercise_minutes": 32,
        "calories": 618,
        "weight": 184.2
    }
