from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base  # ✅ IMPORT, DON'T CREATE


class Student(Base):
    __tablename__ = "students"

    student_id = Column(String, primary_key=True)
    name = Column(String)
    grade = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class AcademicEvent(Base):
    __tablename__ = "academic_events"

    event_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, ForeignKey("students.student_id"))
    event_type = Column(String)
    subject = Column(String)
    value = Column(Float)
    timestamp = Column(DateTime)
    source = Column(String)


class DigitalTwin(Base):
    __tablename__ = "digital_twins"

    student_id = Column(String, ForeignKey("students.student_id"), primary_key=True)

    attendance_avg = Column(Float, default=0.0)
    math_avg = Column(Float, default=0.0)
    science_avg = Column(Float, default=0.0)
    english_avg = Column(Float, default=0.0)
    homework_avg = Column(Float, default=0.0)
    behavior_score = Column(Float, default=0.0)
    performance_trend = Column(Float, default=0.0)

    risk_level = Column(String, default="Low")
    failure_probability = Column(Float, default=0.0)
    predicted_score = Column(Float, default=0.0)
    decision = Column(String, default="Monitor")

    triggered_rules = Column(JSON, default=list)
    recommendations = Column(JSON, default=list)

    last_updated = Column(DateTime, default=datetime.utcnow)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)

    students = relationship("ParentStudent", back_populates="parent")


class ParentStudent(Base):
    __tablename__ = "parent_student"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    student_id = Column(String, ForeignKey("students.student_id"), nullable=False)

    parent = relationship("User", back_populates="students")
    student = relationship("Student")
