import { useAuth } from "../auth/AuthContext";

export function Topbar() {
  const { user, logout } = useAuth();

  return (
    <header
      style={{
        height: 56,
        background: "#ffffff",
        borderBottom: "1px solid #bbbec4",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        padding: "0 24px",
      }}
    >
      <strong>Gestão de Licitações</strong>

      <div style={{ display: "flex", gap: 12, alignItems: "center" }}>
        <span>
          {user?.nome} ({user?.role})
        </span>
        <button onClick={logout}>Sair</button>
      </div>
    </header>
  );
}
