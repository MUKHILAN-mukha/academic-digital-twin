export default function Charts({ twin }) {
  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <h3 className="font-semibold mb-4">Performance Snapshot</h3>

      <ul className="space-y-2">
        <li>📈 Performance Trend: {twin.performance_trend}</li>
        <li>🎯 Predicted Score: {twin.predicted_score}</li>
        <li>⚠ Failure Probability: {twin.failure_probability}</li>
      </ul>
    </div>
  );
}
