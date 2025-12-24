from risk_rules import assess_risk
from forecasting import forecast_performance
from decision_engine import generate_decision
import json

def run_pipeline(twin):
    risk_level, rules = assess_risk(twin)
    predicted_score, grade, failure_prob = forecast_performance(twin)
    decision_output = generate_decision(
        twin["student_id"],
        risk_level,
        failure_prob,
        rules
    )

    return {
        "student_id": twin["student_id"],
        "risk_level": risk_level,
        "triggered_rules": rules,
        "predicted_final_score": predicted_score,
        "grade_range": grade,
        "failure_probability": failure_prob,
        "decision": decision_output["decision"],
        "recommendations": decision_output["recommendations"]
    }


if __name__ == "__main__":
    with open("sample_twin.json") as f:
        twin_data = json.load(f)

    result = run_pipeline(twin_data)
    print(json.dumps(result, indent=2))
