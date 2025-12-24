def run_intelligence_engine(twin):
    attendance = twin.attendance_avg or 0
    math = twin.math_avg or 0
    science = twin.science_avg or 0

    risk_level = "Low"
    failure_probability = 0.1
    decision = "Normal"

    triggered_rules = []
    recommendations = []

    if attendance < 75:
        triggered_rules.append("Low Attendance")
        recommendations.append("Improve attendance consistency")
        failure_probability += 0.2

    if math < 40:
        triggered_rules.append("Low Math Performance")
        recommendations.append("Assign math remedial classes")
        failure_probability += 0.3

    if failure_probability >= 0.5:
        risk_level = "High"
        decision = "Immediate Intervention"
    elif failure_probability >= 0.3:
        risk_level = "Moderate"
        decision = "Monitor"

    predicted_score = int((math + science) / 2)

    return {
        "risk_level": risk_level,
        "failure_probability": round(failure_probability, 2),
        "predicted_score": predicted_score,
        "decision": decision,
        "triggered_rules": triggered_rules,
        "recommendations": recommendations
    }
