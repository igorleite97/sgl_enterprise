import { Routes, Route } from "react-router-dom";
import { LoginPage } from "../pages/LoginPage";
import { DashboardPage } from "../pages/DashboardPage";
import { CaptacaoPage } from "../pages/CaptacaoPage";
import { CaptacaoDetalhePage } from "@/app/pages/CaptacaoDetalhePage";
import { AnaliseEditalPage } from "@/app/pages/AnaliseEditalPage.tsx";
import { ProtectedRoute } from "../auth/ProtectedRoute";
import { AppLayout } from "../layout/AppLayout";

export function AppRoutes() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />

      <Route
        element={
          <ProtectedRoute>
            <AppLayout />
          </ProtectedRoute>
        }
      >
        <Route path="/" element={<DashboardPage />} />
        <Route path="/captacao" element={<CaptacaoPage />} />
        <Route path="/captacao/:id" element={<CaptacaoDetalhePage />} />
        <Route
          path="/captacao/:id/analise-edital"
          element={<AnaliseEditalPage />}
        />
      </Route>

      <Route path="*" element={<LoginPage />} />
    </Routes>
  );
}
