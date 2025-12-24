export const twinData = {
  student_id: "STD101",
  grade: "Class 10",
  last_updated: "12 Sep 2025, 10:45 AM",

  attendance: 72,
  homework: 45,
  avg_score: 52,
  predicted_score: 52,
  failure_probability: 0.45,

  risk_level: "HIGH",
  triggered_rules: [
    "Low Attendance",
    "Math Below Pass Mark",
    "Low Homework Completion"
  ],

  decision: "IMMEDIATE INTERVENTION",
  recommendations: [
    "Parent-teacher meeting",
    "Math remedial classes",
    "Attendance monitoring"
  ],

  alerts: [
    {
      date: "12 Sep",
      type: "High Risk",
      severity: "High",
      recipient: "Parent",
      status: "Sent"
    },
    {
      date: "10 Sep",
      type: "Attendance Drop",
      severity: "Medium",
      recipient: "Teacher",
      status: "Sent"
    }
  ]
};
