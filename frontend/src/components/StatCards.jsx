import React from "react";

const StatCards = ({ assets }) => {
  const total = assets.length;
  const available = assets.filter(a => a.status === "Available").length;
  const assigned = assets.filter(a => a.status === "Assigned").length;

  return (
    <div style={{ display: "flex", gap: "20px", marginBottom: "20px" }}>
      <div style={cardStyle}>
        <h3>Total Assets</h3>
        <p>{total}</p>
      </div>

      <div style={cardStyle}>
        <h3>Available</h3>
        <p>{available}</p>
      </div>

      <div style={cardStyle}>
        <h3>Assigned</h3>
        <p>{assigned}</p>
      </div>
    </div>
  );
};

const cardStyle = {
  padding: "20px",
  background: "#f3f3f3",
  borderRadius: "10px",
  width: "150px",
  textAlign: "center"
};

export default StatCards;