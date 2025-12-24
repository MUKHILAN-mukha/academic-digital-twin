from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

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
