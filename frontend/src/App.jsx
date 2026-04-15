import { useEffect, useState } from "react";
import { getAssets } from "./api";

// Components
import Sidebar from "./components/Sidebar";
import AssetsTable from "./components/AssetsTable";
import StatCards from "./components/StatCards";

function App() {
  const [assets, setAssets] = useState([]);
  const [role, setRole] = useState("admin"); // admin / employee
  const [theme, setTheme] = useState("light");

  // Fetch assets
  useEffect(() => {
    getAssets().then(setAssets);
  }, []);

  // Theme toggle handler
  const toggleTheme = () => {
    setTheme(theme === "light" ? "dark" : "light");
  };

  // Dynamic styles
  const isDark = theme === "dark";

  const appStyle = {
    display: "flex",
    backgroundColor: isDark ? "#121212" : "#f5f5f5",
    color: isDark ? "#ffffff" : "#000000",
    minHeight: "100vh",
  };

  const contentStyle = {
    padding: "20px",
    width: "100%",
  };

  const buttonStyle = {
    marginRight: "10px",
    padding: "8px 12px",
    cursor: "pointer",
    border: "none",
    borderRadius: "5px",
  };

  return (
    <div style={appStyle}>
      {/* Sidebar */}
      <Sidebar role={role} />

      {/* Main Content */}
      <div style={contentStyle}>
        <h1>Dashboard</h1>

        {/* Top Controls */}
        <div style={{ marginBottom: "20px" }}>
          <button style={buttonStyle} onClick={() => setRole("admin")}>
            Admin
          </button>

          <button style={buttonStyle} onClick={() => setRole("employee")}>
            Employee
          </button>

          <button style={buttonStyle} onClick={toggleTheme}>
            Toggle Theme ({theme})
          </button>
        </div>

        {/* Stats */}
        <StatCards assets={assets} />

        {/* Table */}
        <AssetsTable assets={assets} role={role} />
      </div>
    </div>
  );
}

export default App;