const menu = [
  { name: "Dashboard", roles: ["admin", "employee"] },
  { name: "Manage Assets", roles: ["admin"] },
  { name: "Employees", roles: ["admin"] },
  { name: "My Assets", roles: ["employee"] },
];

function Sidebar({ role }) {
  return (
    <div style={{ width: "200px", background: "#222", color: "white", padding: "20px" }}>
      <h2>Asset Manager</h2>

      {menu
        .filter(item => item.roles.includes(role))
        .map(item => (
          <div key={item.name} style={{ margin: "10px 0" }}>
            {item.name}
          </div>
        ))}
    </div>
  );
}

export default Sidebar;