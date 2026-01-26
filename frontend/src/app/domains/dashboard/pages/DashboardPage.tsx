import { useAuth } from "../../../auth/AuthContext";

export function DashboardPage() {
  const { user, logout } = useAuth();

  return (
    <div style={{ padding: 40 }}>
      <h2>Dashboard</h2>
      <p>Usuário: {user?.nome}</p>
      <p>Perfil: {user?.role}</p>

      <button onClick={logout}>Logout</button>
    </div>
  );
}
