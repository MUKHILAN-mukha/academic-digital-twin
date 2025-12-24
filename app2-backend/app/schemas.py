from pydantic import BaseModel
from datetime import datetime
from typing import List

# 🚀 Auth
class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class UserResponse(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

# 📌 Event schemas
class AcademicEventCreate(BaseModel):
    student_id: str
    event_type: str
    subject: str | None = None
    value: float
    timestamp: datetime
    source: str

# 📌 Twin response
class DigitalTwinResponse(BaseModel):
    student_id: str

    attendance_avg: float
    math_avg: float
    science_avg: float
    english_avg: float
    homework_avg: float
    behavior_score: float
    performance_trend: float

    risk_level: str
    failure_probability: float
    predicted_score: float
    decision: str

    triggered_rules: List[str]
    recommendations: List[str]

    last_updated: datetime

    class Config:
        from_attributes = True

class ParentStudentCreate(BaseModel):
    parent_id: int
    student_id: str
