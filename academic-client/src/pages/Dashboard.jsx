import { useState } from "react";
import AcademicForm from "../components/AcademicForm";

function Dashboard() {
  const [lastEventTime, setLastEventTime] = useState(null);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-100 to-slate-200">
      
      {/* Top Header */}
      <header className="border-b bg-white/70 backdrop-blur">
        <div className="max-w-7xl mx-auto px-8 py-6 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold">
              Academic Data Entry Dashboard
            </h1>
            <p className="text-sm text-slate-600">
              Digital Twin – Student Academic Monitoring System
            </p>
          </div>

          {/* Status Badge */}
          <div className="text-sm">
            <span className="px-3 py-1 rounded-full bg-green-100 text-green-700 font-medium">
              System Online
            </span>
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="max-w-7xl mx-auto px-8 py-12 grid grid-cols-12 gap-8">

        {/* Left: Form */}
        <section className="col-span-12 lg:col-span-8">
          <AcademicForm
            onEventCreate={() => {
              setLastEventTime(new Date().toLocaleTimeString());
            }}
          />
        </section>

        {/* Right: Info Panel */}
        <aside className="col-span-12 lg:col-span-4 space-y-6">

          {/* System Info Card */}
          <div className="bg-white rounded-xl shadow p-6">
            <h3 className="font-semibold mb-2">System Info</h3>
            <ul className="text-sm text-slate-600 space-y-1">
              <li>Mode: Academic Digital Twin</li>
              <li>Data Source: Manual Entry</li>
              <li>Backend: Connected</li>
            </ul>
          </div>

          {/* Last Event Card */}
          <div className="bg-white rounded-xl shadow p-6">
            <h3 className="font-semibold mb-2">Last Event</h3>
            <p className="text-sm text-slate-600">
              {lastEventTime
                ? `Last academic event recorded at ${lastEventTime}`
                : "No events recorded yet"}
            </p>
          </div>

          {/* Placeholder for Future */}
          <div className="bg-white rounded-xl shadow p-6 border-dashed border-2 border-slate-200">
            <h3 className="font-semibold mb-2">Coming Soon</h3>
            <p className="text-sm text-slate-500">
              Performance trends, risk indicators, and reports will appear here.
            </p>
          </div>

        </aside>
      </main>
    </div>
  );
}

export default Dashboard;
