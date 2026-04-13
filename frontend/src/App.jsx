import { useState } from "react";
import Sidebar from "./components/Sidebar";
import ThemeToggle from "./components/ThemeToggle";

function App() {
  const [role, setRole] = useState("admin"); // change to "employee" to test

  return (
    <div style={{ display: "flex" }}>
      <Sidebar role={role} />

      <div style={{ padding: "20px" }}>
        <h1>Dashboard
          <ThemeToggle />
        </h1>

        <button onClick={() => setRole("admin")}>Admin View</button>
        <button onClick={() => setRole("employee")}>Employee View</button>
      </div>
    </div>
  );
}

export default App;