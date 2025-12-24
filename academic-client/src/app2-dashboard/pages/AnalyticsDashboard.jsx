import { useEffect, useState } from "react";
import { fetchDigitalTwin } from "../../services/digitalTwinApi";

import RiskBadge from "../components/RiskBadge";
import StatCard from "../components/StatCard";
import ActionList from "../components/ActionList";
import AlertsTable from "../components/AlertsTable";
import Charts from "../components/Charts";

function AnalyticsDashboard() {
  const [twinData, setTwinData] = useState(null);
  const [error, setError] = useState(null);

  // Fetch from backend
  useEffect(() => {
    fetchDigitalTwin("STD101")
      .then(setTwinData)
      .catch(() => setError("Failed to load digital twin"));
  }, []);

  // Error state
  if (error) {
    return <div className="p-10 text-red-600">{error}</div>;
  }

  // Loading state
  if (!twinData) {
    return <div className="p-10">Loading digital twin…</div>;
  }

  return (
    <div className="min-h-screen bg-slate-100 p-8 space-y-8">

      {/* Header */}
      <header className="bg-white rounded-xl shadow p-6 flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold">
            Academic Digital Twin – Analytics Dashboard
          </h1>
          <p className="text-sm text-slate-600">
            Student Performance & Risk Monitoring
          </p>
        </div>

        {/* Temporary risk (until ML engine plugs in) */}
        <RiskBadge level="Moderate" />
      </header>

      {/* Student Info */}
      <section className="bg-white rounded-xl shadow p-6 flex justify-between items-center">
        <div>
          <p className="text-sm text-slate-500">Student ID</p>
          <p className="text-xl font-semibold">{twinData.student_id}</p>
        </div>

        <p className="text-sm text-slate-500">
          Last Updated: {twinData.last_updated}
        </p>
      </section>

      {/* Stats (mapped to current backend fields) */}
      <section className="grid grid-cols-2 md:grid-cols-4 gap-6">
        <StatCard
          label="Attendance"
          value={`${twinData.attendance_avg ?? 0}%`}
        />
        <StatCard
          label="Math Avg"
          value={twinData.math_avg ?? "N/A"}
        />
        <StatCard
          label="Science Avg"
          value={twinData.science_avg ?? "N/A"}
        />
        <StatCard
          label="Homework Avg"
          value={`${twinData.homework_avg ?? 0}%`}
        />
      </section>

      {/* Intelligence (safe placeholders for now) */}
      <section className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <ActionList
          decision="Monitor"
          rules={[]}
          recommendations={[
            "Improve attendance",
            "Focus on weak subjects",
          ]}
        />

        <Charts />
      </section>

      {/* Alerts */}
      <section>
        <AlertsTable alerts={[]} />
      </section>

    </div>
  );
}

export default AnalyticsDashboard;
