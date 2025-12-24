from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User, Student, ParentStudent
from app.services.role_checker import require_roles

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/assign-student")
def assign_student_to_parent(
    parent_username: str,
    student_id: str,
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles(["ADMIN"]))
):
    parent = db.query(User).filter(User.username == parent_username).first()
    if not parent or parent.role != "PARENT":
        raise HTTPException(status_code=404, detail="Parent not found")

    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    existing = db.query(ParentStudent).filter(
        ParentStudent.parent_id == parent.id,
        ParentStudent.student_id == student_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already assigned")

    mapping = ParentStudent(parent_id=parent.id, student_id=student_id)
    db.add(mapping)
    db.commit()

    return {"message": "Student assigned to parent successfully"}
