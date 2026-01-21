import { NavLink } from "react-router-dom";

const menu = [
  { label: "Dashboard", path: "/" },
  { label: "Captação", path: "/captacao" },
  { label: "Editais", path: "/editais" },
  { label: "Cotações", path: "/cotacoes" },
  { label: "Disputa", path: "/disputa" },
  { label: "Pós-Pregão", path: "/pos-pregao" },
  { label: "Contratos", path: "/contratos" },
];

export function Sidebar() {
  return (
    <aside
      style={{
        width: 240,
        background: "#1f2d3d",
        color: "#e6e6e6ec",
        padding: 20,
      }}
    >
      <h2 style={{ marginBottom: 24 }}>SGL</h2>

      <nav style={{ display: "flex", flexDirection: "column", gap: 15 }}>
        {menu.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            style={({ isActive }) => ({
              color: isActive ? "#3371bd" : "#eeeeee",
              textDecoration: "none",
              fontWeight: isActive ? "bold" : "normal",
            })}
          >
            {item.label}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}
