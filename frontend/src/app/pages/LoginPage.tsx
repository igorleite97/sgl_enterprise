import { useNavigate } from "react-router-dom";
import { useAuth } from "@/app/auth/AuthContext";

export function LoginPage() {
  const { login } = useAuth();
  const navigate = useNavigate();

  function handleLogin() {
    login("ANALISTA");
    navigate("/dashboard"); // ⬅️ ESSENCIAL
  }

  return (
    <div style={{ padding: 32 }}>
      <h1>Login</h1>

      <button onClick={handleLogin}>
        Entrar como Analista
      </button>
    </div>
  );
}
