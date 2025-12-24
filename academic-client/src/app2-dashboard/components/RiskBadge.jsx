export default function RiskBadge({ level, decision }) {
  const colorMap = {
    Low: "bg-green-100 text-green-700",
    Medium: "bg-yellow-100 text-yellow-700",
    High: "bg-red-100 text-red-700"
  };

  return (
    <div className={`p-4 rounded-lg ${colorMap[level]}`}>
      <h2 className="text-xl font-semibold">Risk Level: {level}</h2>
      <p className="text-sm mt-1">{decision}</p>
    </div>
  );
}
