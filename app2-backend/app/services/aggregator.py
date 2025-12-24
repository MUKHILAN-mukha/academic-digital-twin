from sqlalchemy.orm import Session
from datetime import datetime

from app.models import AcademicEvent, DigitalTwin
from app.services.risk_engine import evaluate_risk
from app.services.prediction_engine import (
    predict_score,
    predict_failure_probability
)


def update_digital_twin(student_id: str, db: Session):
    """
    Recomputes and updates the digital twin state for a student
    """

    events = db.query(AcademicEvent).filter(
        AcademicEvent.student_id == student_id
    ).all()

    if not events:
        return None

    # ---------- Attendance ----------
    attendance_events = [e for e in events if e.event_type == "attendance"]
    attendance_avg = (
        sum(e.value for e in attendance_events) / len(attendance_events) * 100
        if attendance_events else 0.0
    )

    # ---------- Homework ----------
    homework_events = [e for e in events if e.event_type == "homework"]
    homework_avg = (
        sum(e.value for e in homework_events) / len(homework_events) * 100
        if homework_events else 0.0
    )

    # ---------- Subject Averages ----------
    def subject_avg(subject_name: str) -> float:
        subject_events = [
            e for e in events
            if e.event_type == "test"
            and e.subject
            and e.subject.lower() == subject_name.lower()
        ]
        return (
            sum(e.value for e in subject_events) / len(subject_events)
            if subject_events else 0.0
        )

    math_avg = subject_avg("math")
    science_avg = subject_avg("science")
    english_avg = subject_avg("english")

    # ---------- Behavior ----------
    behavior_events = [e for e in events if e.event_type == "behavior"]
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

    # ---------- RISK ENGINE ----------
    (
        risk_level,
        _risk_failure_probability,
        decision,
        triggered_rules,
        recommendations
    ) = evaluate_risk(
        attendance_avg=attendance_avg,
        math_avg=math_avg,
        science_avg=science_avg,
        english_avg=english_avg,
        homework_avg=homework_avg,
        behavior_score=behavior_score,
        performance_trend=performance_trend
    )

    # ---------- PREDICTION ENGINE (🔥 MISSING PART FIXED) ----------
    predicted_score = predict_score(
        math_avg=math_avg,
        science_avg=science_avg,
        english_avg=english_avg,
        attendance_avg=attendance_avg,
        homework_avg=homework_avg,
        behavior_score=behavior_score,
        performance_trend=performance_trend
    )

    failure_probability = predict_failure_probability(predicted_score)

    # ---------- Update or Create Digital Twin ----------
    twin = db.query(DigitalTwin).filter(
        DigitalTwin.student_id == student_id
    ).first()

    if not twin:
        twin = DigitalTwin(student_id=student_id)
        db.add(twin)

    # Aggregates
    twin.attendance_avg = attendance_avg
    twin.homework_avg = homework_avg
    twin.math_avg = math_avg
    twin.science_avg = science_avg
    twin.english_avg = english_avg
    twin.behavior_score = behavior_score
    twin.performance_trend = performance_trend

    # Intelligence
    twin.risk_level = risk_level
    twin.predicted_score = predicted_score
    twin.failure_probability = failure_probability
    twin.decision = decision
    twin.triggered_rules = triggered_rules
    twin.recommendations = recommendations

    twin.last_updated = datetime.utcnow()

    db.commit()
    return twin
