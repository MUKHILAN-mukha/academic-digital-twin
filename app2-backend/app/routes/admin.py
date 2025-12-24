from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Student, User
from app.services.auth_utils import get_current_user

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create-student")
def create_student(
    student_id: str,
    name: str,
    grade: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Admins only")

    existing = db.query(Student).filter(Student.student_id == student_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Student already exists")

    student = Student(
        student_id=student_id,
        name=name,
        grade=grade
    )
    db.add(student)
    db.commit()

    return {"message": "Student created"}
