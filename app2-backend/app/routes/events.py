from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.aggregator import update_digital_twin
from app.database import SessionLocal
from app.models import AcademicEvent, Student
from app.schemas import AcademicEventCreate

router = APIRouter(prefix="/events", tags=["Events"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_event(event: AcademicEventCreate, db: Session = Depends(get_db)):
    # Ensure student exists
    student = db.query(Student).filter(
        Student.student_id == event.student_id
    ).first()

    if not student:
        student = Student(
            student_id=event.student_id,
            name="Unknown",
            grade="Class 10"
        )
        db.add(student)
        db.commit()

    new_event = AcademicEvent(
        student_id=event.student_id,
        event_type=event.event_type,
        subject=event.subject,
        value=event.value,
        timestamp=event.timestamp,
        source=event.source
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    # 🔁 Update Digital Twin
    update_digital_twin(event.student_id, db)

    return {
        "message": "Event recorded and digital twin updated",
        "event_id": new_event.event_id
    }

