import { Navigate } from "react-router-dom";
import { useAuth } from "@/app/auth/AuthContext";
import type { ReactNode } from "react";

export function ProtectedRoute({ children }: { children: ReactNode }) {
  const { user, loading } = useAuth();

  console.log("AUTH STATE", { loading, isAuthenticated: !!user });

  // ⏳ Enquanto restaura sessão, não decide nada
  if (loading) {
    return <p>Carregando sessão...</p>;
  }

  // 🔒 Só bloqueia se realmente NÃO houver usuário
  if (!user) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
}
