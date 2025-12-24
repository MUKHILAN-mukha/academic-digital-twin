function ActionList({ decision, rules = [], recommendations = [] }) {
  return (
    <div className="bg-white p-6 rounded-xl shadow">
      <h3 className="font-semibold mb-2">System Decision</h3>
      <p className="text-red-600 font-bold">{decision}</p>

      <p className="mt-4 font-medium text-sm">Triggered Risks:</p>
      <ul className="list-disc list-inside text-sm text-slate-600">
        {rules.map((r, i) => (
          <li key={i}>{r}</li>
        ))}
      </ul>

      <p className="mt-4 font-medium text-sm">Recommended Actions:</p>
      <ul className="list-disc list-inside text-sm text-slate-600">
        {recommendations.map((r, i) => (
          <li key={i}>{r}</li>
        ))}
      </ul>
    </div>
  );
}

export default ActionList;
