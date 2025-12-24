from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ---------- REQUEST SCHEMA (POST /events) ----------
class AcademicEventCreate(BaseModel):
    student_id: str
    event_type: str          # attendance, test, homework, behavior
    subject: Optional[str] = None
    value: float
    timestamp: datetime
    source: Optional[str] = "manual"


# ---------- RESPONSE SCHEMA (GET /digital-twin) ----------
class DigitalTwinResponse(BaseModel):
    student_id: str
    attendance_avg: float | None
    math_avg: float | None
    science_avg: float | None
    english_avg: float | None
    homework_avg: float | None
    behavior_score: float | None
    performance_trend: float | None
    last_updated: datetime

    # 🔥 Member 3 fields
    risk_level: str
    failure_probability: float
    predicted_score: int
    decision: str
    triggered_rules: list[str]
    recommendations: list[str]

    class Config:
        from_attributes = True

