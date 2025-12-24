function AlertsTable({ alerts }) {
  return (
    <div className="bg-white rounded-xl shadow p-6">
      <h3 className="font-semibold mb-4">Alerts & Logs</h3>

      <table className="w-full text-sm">
        <thead>
          <tr className="text-slate-500 border-b">
            <th className="text-left py-2">Date</th>
            <th>Type</th>
            <th>Severity</th>
            <th>Recipient</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {alerts.map((a, i) => (
            <tr key={i} className="border-b last:border-none">
              <td className="py-2">{a.date}</td>
              <td className="text-center">{a.type}</td>
              <td className="text-center">{a.severity}</td>
              <td className="text-center">{a.recipient}</td>
              <td className="text-center">{a.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AlertsTable;
