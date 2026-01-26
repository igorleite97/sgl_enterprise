import { createContext, useContext, useState, useEffect } from "react";
import type { ReactNode } from "react";

export type Role = "ANALISTA" | "GESTOR" | "ADMIN";

interface User {
  nome: string;
  role: Role;
}

interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  loading: boolean;
  login: (role: Role) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  // 🔁 Restaura sessão
  useEffect(() => {
    const saved = localStorage.getItem("sgl:user");
    if (saved) {
      setUser(JSON.parse(saved));
    }
    setLoading(false);
  }, []);

  function login(role: Role) {
    const user = { nome: "Usuário Mock", role };
    setUser(user);
    localStorage.setItem("sgl:user", JSON.stringify(user));
  }

  function logout() {
    setUser(null);
    localStorage.removeItem("sgl:user");
  }

  return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated: !!user,
        loading,
        login,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth deve ser usado dentro de AuthProvider");
  }
  return context;
}
