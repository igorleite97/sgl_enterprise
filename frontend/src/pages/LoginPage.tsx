import { useAuth } from "../auth/AuthContext";
import { useNavigate } from "react-router-dom";

export const LoginPage = () => {
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleLogin = () => {
    login({
      id: "u-001",
      nome: "Analista",
      perfil: "ANALISTA",
    });

    navigate("/");
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>SGL Enterprise</h1>
      <button onClick={handleLogin}>Entrar (mock)</button>
    </div>
  );
};
