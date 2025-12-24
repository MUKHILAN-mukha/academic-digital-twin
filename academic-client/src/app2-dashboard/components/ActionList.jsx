export default function ActionList({ actions }) {
  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <h3 className="font-semibold mb-2">Recommended Actions</h3>

      <ul className="list-disc ml-5 space-y-1">
        {actions.map((a, i) => (
          <li key={i}>{a}</li>
        ))}
      </ul>
    </div>
  );
}
