def generate_decision(student_id, risk_level, failure_prob, rules):
    recommendations = []

    if risk_level == "LOW" and failure_prob < 0.3:
        decision = "MONITOR"
        recommendations += [
            "Continue current study plan",
            "Monthly academic review"
        ]

    elif risk_level == "MODERATE":
        decision = "REMEDIAL_ACTION"
        recommendations += [
            "Enroll in remedial classes",
            "Provide additional practice materials",
            "Weekly progress tracking"
        ]

    else:
        decision = "IMMEDIATE_INTERVENTION"
        recommendations += [
            "Immediate parent-teacher meeting",
            "One-on-one academic counseling",
            "Daily monitored study plan"
        ]

    if "Low Attendance" in rules:
        recommendations.append("Strict attendance monitoring")

    for rule in rules:
        if "Math" in rule:
            recommendations.append("Dedicated Math remedial sessions")
        if "Science" in rule:
            recommendations.append("Dedicated Science remedial sessions")

    return {
        "student_id": student_id,
        "decision": decision,
        "recommendations": recommendations
    }
