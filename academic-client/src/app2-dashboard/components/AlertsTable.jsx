export default function AlertsTable({ rules }) {
  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <h3 className="font-semibold mb-2">Alerts</h3>

      {rules.length === 0 ? (
        <p>No alerts 🎉</p>
      ) : (
        <ul className="list-disc ml-5">
          {rules.map((r, i) => (
            <li key={i}>{r}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
