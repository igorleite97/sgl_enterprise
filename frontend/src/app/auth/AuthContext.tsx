import { createContext, useContext, useState } from "react";

type User = {
  id: string;
  nome: string;
  role: "ANALISTA" | "GESTOR" | "ADMIN";
};

type AuthContextType = {
  user: User | null;
  login: (email: string, senha: string) => Promise<void>;
  logout: () => void;
};

const AuthContext = createContext<AuthContextType>({} as AuthContextType);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);

  async function login(email: string, senha: string) {
    // PROVISÓRIO (mock)
    setUser({
      id: "1",
      nome: "Igor Leite",
      role: "ADMIN",
    });
  }

  function logout() {
    setUser(null);
  }

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
