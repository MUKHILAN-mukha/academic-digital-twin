from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import DigitalTwin, ParentStudent, User
from app.schemas import DigitalTwinResponse
from app.services.auth_utils import get_current_user

router = APIRouter(prefix="/digital-twin", tags=["Digital Twin"])


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{student_id}", response_model=DigitalTwinResponse)
def get_digital_twin(
    student_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Fetch digital twin
    twin = db.query(DigitalTwin).filter(
        DigitalTwin.student_id == student_id
    ).first()

    if not twin:
        raise HTTPException(status_code=404, detail="Digital twin not found")

    # 🔐 ROLE-BASED ACCESS CONTROL

    # STUDENT → only own data
    if current_user.role == "STUDENT":
        if current_user.student_id != student_id:
            raise HTTPException(status_code=403, detail="Access denied")

    # PARENT → only mapped children
    if current_user.role == "PARENT":
        mapping = db.query(ParentStudent).filter(
            ParentStudent.parent_id == current_user.id,
            ParentStudent.student_id == student_id
        ).first()

        if not mapping:
            raise HTTPException(
                status_code=403,
                detail="Child not linked to parent"
            )

    # TEACHER & ADMIN → allowed (future scope: class restriction)

    # ✅ SAFE RESPONSE (matches schema exactly)
    return {
        "student_id": twin.student_id,
        "attendance_avg": twin.attendance_avg,
        "math_avg": twin.math_avg,
        "science_avg": twin.science_avg,
        "homework_avg": twin.homework_avg,
        "last_updated": twin.last_updated,

        "risk_level": twin.risk_level,
        "failure_probability": twin.failure_probability,
        "predicted_score": twin.predicted_score,
        "decision": twin.decision,
        "triggered_rules": twin.triggered_rules or [],
        "recommendations": twin.recommendations or []
    }
