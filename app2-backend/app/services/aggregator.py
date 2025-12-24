from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime

from app.models import AcademicEvent, DigitalTwin


def update_digital_twin(student_id: str, db: Session):
    """
    Recomputes and updates the digital twin state for a student
    """

    # Fetch all events for the student
    events = db.query(AcademicEvent).filter(
        AcademicEvent.student_id == student_id
    ).all()

    if not events:
        return None

    # ---------- Attendance ----------
    attendance_events = [
        e for e in events if e.event_type == "attendance"
    ]
    attendance_avg = (
        sum(e.value for e in attendance_events) / len(attendance_events) * 100
        if attendance_events else 0
    )

    # ---------- Homework ----------
    homework_events = [
        e for e in events if e.event_type == "homework"
    ]
    homework_avg = (
        sum(e.value for e in homework_events) / len(homework_events) * 100
        if homework_events else 0
    )

    # ---------- Subject Averages ----------
    def subject_avg(subject_name):
        subject_events = [
            e for e in events
            if e.event_type == "test" and e.subject == subject_name
        ]
        return (
            sum(e.value for e in subject_events) / len(subject_events)
            if subject_events else None
        )

    math_avg = subject_avg("Math")
    science_avg = subject_avg("Science")
    english_avg = subject_avg("English")

    # ---------- Behavior ----------
    behavior_events = [
        e for e in events if e.event_type == "behavior"
    ]
    behavior_score = (
        sum(e.value for e in behavior_events) / len(behavior_events)
        if behavior_events else 0.5
    )

    # ---------- Performance Trend ----------
    test_events = sorted(
        [e for e in events if e.event_type == "test"],
        key=lambda x: x.timestamp
    )

    performance_trend = 0.0
    if len(test_events) >= 2:
        performance_trend = test_events[-1].value - test_events[0].value

    # ---------- Update or Create Digital Twin ----------
    twin = db.query(DigitalTwin).filter(
        DigitalTwin.student_id == student_id
    ).first()

    if not twin:
        twin = DigitalTwin(student_id=student_id)
        db.add(twin)

    twin.attendance_avg = attendance_avg
    twin.homework_avg = homework_avg
    twin.math_avg = math_avg
    twin.science_avg = science_avg
    twin.english_avg = english_avg
    twin.behavior_score = behavior_score
    twin.performance_trend = performance_trend
    twin.last_updated = datetime.utcnow()

    db.commit()
    return twin
