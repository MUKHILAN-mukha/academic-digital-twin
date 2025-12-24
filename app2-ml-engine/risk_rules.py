def assess_risk(twin):
    triggered_rules = []

    if twin["attendance_avg"] < 75:
        triggered_rules.append("Low Attendance")

    subjects = {
        "Math": twin["math_avg"],
        "Science": twin["science_avg"],
        "English": twin["english_avg"],
    }

    for subject, score in subjects.items():
        if score < 40:
            triggered_rules.append(f"{subject} Below Pass Mark")

    if twin["homework_avg"] < 0.5:
        triggered_rules.append("Low Homework Completion")

    if twin["trend"] < -0.10:
        triggered_rules.append("Performance Decline")

    # Risk classification
    if len(triggered_rules) == 0:
        risk_level = "LOW"
    elif len(triggered_rules) == 1:
        risk_level = "MODERATE"
    else:
        risk_level = "HIGH"

    return risk_level, triggered_rules
