def predict_score(
    math_avg: float,
    science_avg: float,
    english_avg: float,
    attendance_avg: float,
    homework_avg: float,
    behavior_score: float,
    performance_trend: float
) -> float:
    """
    Predict overall academic score (0–100)
    """

    weights = {
        "math": 0.22,
        "science": 0.22,
        "english": 0.18,
        "attendance": 0.15,
        "homework": 0.13,
        "behavior": 0.05,
        "trend": 0.05
    }

    base_score = (
        math_avg * weights["math"]
        + science_avg * weights["science"]
        + english_avg * weights["english"]
        + attendance_avg * weights["attendance"]
        + homework_avg * weights["homework"]
        + (behavior_score * 100) * weights["behavior"]
    )

    trend_adjustment = performance_trend * weights["trend"]

    return round(min(max(base_score + trend_adjustment, 0), 100), 2)



def predict_failure_probability(predicted_score: float) -> float:
    if predicted_score >= 75:
        return 0.05
    elif predicted_score >= 60:
        return 0.2
    elif predicted_score >= 40:
        return 0.5
    else:
        return 0.75
