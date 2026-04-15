export default function Sidebar({ role }) {
  console.log("Sidebar Role:", role);

  return (
    <div style={{
      width: "200px",
      background: "#1e1e1e",
      color: "white",
      padding: "20px"
    }}>
      <h2>Asset Manager</h2>

      <p>Dashboard</p>

      {role === "admin" ? (
        <>
          <p>Manage Assets</p>
          <p>Employees</p>
        </>
      ) : null}
    </div>
  );
}