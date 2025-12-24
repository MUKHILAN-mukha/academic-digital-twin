def forecast_performance(twin):
    weighted_score = (
        twin["attendance_avg"] * 0.2 +
        twin["homework_avg"] * 100 * 0.2 +
        ((twin["math_avg"] + twin["science_avg"] + twin["english_avg"]) / 3) * 0.4 +
        twin["behavior_score"] * 100 * 0.2
    )

    predicted_score = round(weighted_score)

    if predicted_score >= 75:
        grade = "A"
        failure_prob = 0.1
    elif predicted_score >= 60:
        grade = "B"
        failure_prob = 0.25
    elif predicted_score >= 45:
        grade = "C"
        failure_prob = 0.45
    else:
        grade = "D"
        failure_prob = 0.7

    return predicted_score, grade, failure_prob
