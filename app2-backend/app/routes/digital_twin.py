from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import DigitalTwin, ParentStudent, User
from app.schemas import DigitalTwinResponse
from app.services.auth_utils import get_current_user

router = APIRouter(prefix="/digital-twin", tags=["Digital Twin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{student_id}", response_model=DigitalTwinResponse)
def get_digital_twin(student_id: str, db: Session = Depends(get_db)):
    twin = db.query(DigitalTwin).filter(
        DigitalTwin.student_id == student_id
    ).first()

    if not twin:
        raise HTTPException(status_code=404, detail="Digital twin not found")

    return {
        "student_id": twin.student_id,
        "attendance_avg": twin.attendance_avg,
        "math_avg": twin.math_avg,
        "science_avg": twin.science_avg,
        "homework_avg": twin.homework_avg,
        "last_updated": twin.last_updated,

        # 🔽 COMPUTED / STORED INTELLIGENCE
        "risk_level": twin.risk_level,
        "failure_probability": twin.failure_probability,
        "predicted_score": twin.predicted_score,
        "decision": twin.decision,
        "triggered_rules": twin.triggered_rules or [],
        "recommendations": twin.recommendations or []
    }
