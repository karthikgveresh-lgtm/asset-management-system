export default function AssetsTable({ assets, role }) {
  console.log("Table Role:", role);

  return (
    <table border="1" cellPadding="10" style={{ marginTop: "20px", width: "100%" }}>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Status</th>
          {role === "admin" && <th>Actions</th>}
        </tr>
      </thead>

      <tbody>
        {assets.map((a) => (
          <tr key={a.id}>
            <td>{a.id}</td>
            <td>{a.name}</td>
            <td>{a.status}</td>

            {role === "admin" && (
              <td>
                <button>Assign</button>
                <button>Delete</button>
              </td>
            )}
          </tr>
        ))}
      </tbody>
    </table>
  );
}