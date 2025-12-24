import { useAuth } from "./context/AuthContext";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import StudentView from "./app2-dashboard/pages/StudentView";

function App() {
  const auth = useAuth();

  if (!auth) {
    return <p style={{ padding: 40 }}>Auth not ready</p>;
  }

  const { user } = auth;

  if (!user) return <Login />;

  if (user.role === "STUDENT") return <StudentView />;
  return <Dashboard />;
}

export default App;
