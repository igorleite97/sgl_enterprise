import { useAuth } from "../auth/AuthContext";
import { useNavigate } from "react-router-dom";

export function LoginPage() {
  const { login } = useAuth();
  const navigate = useNavigate();

  function handleLogin(role: "ANALISTA" | "GESTOR" | "ADMIN") {
    login(role);
    navigate("/");
  }

  return (
    <div style={{ padding: 40 }}>
      <h1>SGL Enterprise</h1>
      <p>Selecione um perfil para login (mock)</p>

      <div style={{ display: "flex", gap: 12 }}>
        <button onClick={() => handleLogin("ANALISTA")}>
          Analista
        </button>
        <button onClick={() => handleLogin("GESTOR")}>
          Gestor
        </button>
        <button onClick={() => handleLogin("ADMIN")}>
          Administrador
        </button>
      </div>
    </div>
  );
}
