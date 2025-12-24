import { useEffect, useState } from "react";
import { getDigitalTwin } from "../../services/digitalTwinApi";

import RiskBadge from "../components/RiskBadge";
import StatCard from "../components/StatCard";
import Charts from "../components/Charts";
import AlertsTable from "../components/AlertsTable";
import ActionList from "../components/ActionList";

export default function StudentView() {
  const [twin, setTwin] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getDigitalTwin("STD101")
      .then(res => setTwin(res.data))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p className="p-6">Loading digital twin…</p>;
  if (!twin) return <p className="p-6">No data available</p>;

  return (
    <div className="p-6 space-y-6">

      {/* Risk Header */}
      <RiskBadge
        level={twin.risk_level}
        decision={twin.decision}
      />

      {/* Stat Cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <StatCard title="Attendance" value={`${twin.attendance_avg}%`} />
        <StatCard title="Math" value={twin.math_avg} />
        <StatCard title="Science" value={twin.science_avg} />
        <StatCard title="English" value={twin.english_avg} />
      </div>

      {/* Charts */}
      <Charts twin={twin} />

      {/* Alerts & Actions */}
      <div className="grid md:grid-cols-2 gap-6">
        <AlertsTable rules={twin.triggered_rules} />
        <ActionList actions={twin.recommendations} />
      </div>

    </div>
  );
}
