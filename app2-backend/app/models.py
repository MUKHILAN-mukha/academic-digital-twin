from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

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
    attendance_avg = Column(Float)
    math_avg = Column(Float)
    science_avg = Column(Float)
    english_avg = Column(Float)
    homework_avg = Column(Float)
    behavior_score = Column(Float)
    performance_trend = Column(Float)
    last_updated = Column(DateTime, default=datetime.utcnow)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)  # ADMIN, TEACHER, PARENT, STUDENT

    students = relationship("ParentStudent", back_populates="parent")


class ParentStudent(Base):
    __tablename__ = "parent_student"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    student_id = Column(String, ForeignKey("students.student_id"), nullable=False)

    parent = relationship("User")
    student = relationship("Student")
