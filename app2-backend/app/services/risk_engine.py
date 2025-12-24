from typing import List, Tuple


def evaluate_risk(
    attendance_avg: float,
    math_avg: float | None,
    science_avg: float | None,
    english_avg: float | None,
    homework_avg: float,
    behavior_score: float,
    performance_trend: float
) -> Tuple[str, float, str, List[str], List[str]]:
    """
    Rule-based academic risk evaluation.
    Returns:
    (risk_level, failure_probability, decision, triggered_rules, recommendations)
    """

    risk_score = 0
    triggered_rules = []
    recommendations = []

    # ---------- Attendance ----------
    if attendance_avg < 75:
        risk_score += 2
        triggered_rules.append("LOW_ATTENDANCE")
        recommendations.append("Improve attendance consistency")

    # ---------- Subject Performance ----------
    def low_subject(score, name):
        nonlocal risk_score
        if score is not None and score < 40:
            risk_score += 3
            triggered_rules.append(f"LOW_{name.upper()}_SCORE")
            recommendations.append(f"Improve fundamentals in {name}")

    low_subject(math_avg, "Math")
    low_subject(science_avg, "Science")
    low_subject(english_avg, "English")

    # ---------- Homework ----------
    if homework_avg < 60:
        risk_score += 1
        triggered_rules.append("LOW_HOMEWORK_COMPLETION")
        recommendations.append("Increase homework completion rate")

    # ---------- Behavior ----------
    if behavior_score < 0.4:
        risk_score += 2
        triggered_rules.append("BEHAVIORAL_RISK")
        recommendations.append("Behavioral counseling recommended")

    # ---------- Trend ----------
    if performance_trend < 0:
        risk_score += 1
        triggered_rules.append("NEGATIVE_PERFORMANCE_TREND")
        recommendations.append("Monitor recent performance decline")

    # ---------- Risk Level ----------
    if risk_score >= 7:
        risk_level = "High"
        decision = "Immediate Intervention Required"
    elif risk_score >= 4:
        risk_level = "Medium"
        decision = "Close Monitoring Required"
    else:
        risk_level = "Low"
        decision = "Normal Monitoring"

    # ---------- Failure Probability ----------
    failure_probability = min(1.0, risk_score / 10)

    return (
        risk_level,
        failure_probability,
        decision,
        triggered_rules,
        recommendations
    )
