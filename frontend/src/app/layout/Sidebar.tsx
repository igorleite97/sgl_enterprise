import { NavLink } from "react-router-dom";

const linkStyle = ({ isActive }: { isActive: boolean }) => ({
  display: "block",
  padding: "8px 12px",
  borderRadius: 6,
  textDecoration: "none",
  color: isActive ? "#072b7a" : "#002677",
  backgroundColor: isActive ? "#dadbdb" : "transparent",
  fontWeight: isActive ? 600 : 400,
});

export function Sidebar() {
  return (
    <aside style={{ width: 260, padding: 16, borderRight: "1px solid #e5e7eb" }}>
      <h3 style={{ marginBottom: 16 }}>SGL Enterprise</h3>

      <nav style={{ display: "flex", flexDirection: "column", gap: 16 }}>
        {/* DASHBOARD */}
        <div>
          <NavLink to="/dashboard" style={linkStyle}>
            Dashboard
          </NavLink>
        </div>

        {/* PROCESSOS */}
        <div>
          <p style={{ fontSize: 12, fontWeight: 600, color: "#6b7280" }}>
            MÓDULOS DE PROCESSOS
          </p>
          <NavLink to="/captacao" style={linkStyle}>
            Captação
          </NavLink>
          <NavLink to="/analise-edital" style={linkStyle}>
            Análise de Edital
          </NavLink>
          <NavLink to="/cotacao" style={linkStyle}>
            Cotação
          </NavLink>
          <NavLink to="/disputa" style={linkStyle}>
            Disputa
          </NavLink>
          <NavLink to="/pos-pregao" style={linkStyle}>
            Pós-Pregão
          </NavLink>
        </div>

        {/* EXECUÇÃO */}
        <div>
          <p style={{ fontSize: 12, fontWeight: 600, color: "#6b7280" }}>
            EXECUÇÃO
          </p>
          <NavLink to="/contratos" style={linkStyle}>
            Contratos
          </NavLink>
          <NavLink to="/empenhos" style={linkStyle}>
            Empenhos
          </NavLink>
        </div>

        {/* GESTÃO */}
        <div>
          <p style={{ fontSize: 12, fontWeight: 600, color: "#6b7280" }}>
            GESTÃO
          </p>
          <NavLink to="/indicadores" style={linkStyle}>
            Indicadores
          </NavLink>
        </div>
      </nav>
    </aside>
  );
}
