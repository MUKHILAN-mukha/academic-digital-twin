import Login from "./pages/Login";
import EntryDashboard from "./pages/Dashboard";
import AnalyticsDashboard from "./app2-dashboard/pages/AnalyticsDashboard";
import { getRole } from "./services/authStorage";

function App() {
  const role = getRole();

  if (!role) {
    return <Login />;
  }

  if (role === "ADMIN" || role === "STUDENT") {
    return <EntryDashboard />;
  }

  if (role === "TEACHER" || role === "PARENT") {
    return <AnalyticsDashboard />;
  }

  return <Login />;
}

export default App;
