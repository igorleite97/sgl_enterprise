import { NavLink } from "react-router-dom";

const navItem = ({ isActive }: { isActive: boolean }) => ({
  display: "flex",
  alignItems: "center",
  padding: "10px 12px",
  borderRadius: 10,
  textDecoration: "none",
  fontWeight: 600,
  color: isActive ? "#072b7a" : "#0f172a",
  backgroundColor: isActive ? "#e5e7eb" : "transparent",
});

const sectionTitle: React.CSSProperties = {
  fontSize: 12,
  fontWeight: 700,
  color: "#6b7280",
  letterSpacing: 0.5,
  margin: "18px 0 8px",
};

export function Sidebar() {
  return (
    <aside
      style={{
        width: 280,
        padding: 16,
        borderRight: "1px solid #e5e7eb",
        background: "#f8fafc",
      }}
    >
      <div style={{ marginBottom: 18 }}>
        <div style={{ fontWeight: 800, fontSize: 16 }}>SGL Enterprise</div>
        <div style={{ fontSize: 12, color: "#6b7280" }}>
          Sistema de Gestão de Licitações
        </div>
      </div>

      <div style={sectionTitle}>MÓDULOS CORE</div>

      <nav style={{ display: "grid", gap: 8 }}>
        <NavLink to="/dashboard" style={navItem}>
          Dashboard
        </NavLink>

        <NavLink to="/captacao" style={navItem}>
          Captação
        </NavLink>

        <NavLink to="/analise-edital" style={navItem}>
          Análise de Edital
        </NavLink>

        {/* Se cotação já estiver pronta, mantenha */}
        <NavLink to="/cotacao" style={navItem}>
          Cotação
        </NavLink>
      </nav>
    </aside>
  );
}
