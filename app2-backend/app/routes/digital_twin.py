from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import DigitalTwin
from app.schemas import DigitalTwinResponse
from app.services.ml_engine import run_intelligence_engine

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
        raise HTTPException(
            status_code=404,
            detail="Digital twin not found for student"
        )

    # Member 3: Intelligence layer
    ml_result = run_intelligence_engine(twin)

    # Combine Twin + ML output
    return {
        "student_id": twin.student_id,
        "attendance_avg": twin.attendance_avg,
        "math_avg": twin.math_avg,
        "science_avg": twin.science_avg,
        "english_avg": twin.english_avg,
        "homework_avg": twin.homework_avg,
        "behavior_score": twin.behavior_score,
        "performance_trend": twin.performance_trend,
        "last_updated": twin.last_updated,

        # ML outputs
        **ml_result
    }
