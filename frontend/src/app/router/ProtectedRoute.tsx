// src/app/router/ProtectedRoute.tsx
import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "@/app/auth/AuthContext";

export function ProtectedRoute() {
  const { isAuthenticated, loading } = useAuth();

  if (loading) {
    return <div style={{ padding: 24 }}>Carregando...</div>;
  }

  if (!isAuthenticated) return <Navigate to="/login" replace />;

  return <Outlet />;
}
