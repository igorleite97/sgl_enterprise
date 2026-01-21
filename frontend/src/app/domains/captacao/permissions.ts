import type { Role } from "../../auth/AuthContext";

export function podeCriarCaptacao(role: Role): boolean {
  return ["ANALISTA", "GESTOR", "ADMIN"].includes(role);
}

export function podeAlterarStatusCaptacao(role: Role): boolean {
  return ["GESTOR", "ADMIN"].includes(role);
}
