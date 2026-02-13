import { Routes, Route } from "react-router-dom";

import { LoginPage } from "@/app/pages/LoginPage";
import { DashboardPage } from "@/app/domains/dashboard/pages/DashboardPage";

import { CaptacaoPage } from "@/app/domains/captacao/pages/CaptacaoPage";
import { CaptacaoDetalhePage } from "@/app/domains/captacao/pages/CaptacaoDetalhePage";

import { AnaliseEditalListPage } 
  from "@/app/domains/analiseEdital/pages/AnaliseEditalListPage";

import { AnaliseEditalPage } 
  from "@/app/domains/analiseEdital/pages/AnaliseEditalPage";

import { ProtectedRoute } from "@/app/router/ProtectedRoute";
import { AppLayout } from "@/app/layout/AppLayout";
import { CotacaoModulePage } from "@/app/domains/cotacao/pages";

export function AppRouter() {
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
        <Route path="/dashboard" element={<DashboardPage />} />

        {/* Captação */}
        <Route path="/captacao" element={<CaptacaoPage />} />
        <Route path="/captacao/:id" element={<CaptacaoDetalhePage />} />

        {/* Análise de Edital */}
        <Route path="/analise-edital" element={<AnaliseEditalListPage />} />
        <Route
          path="/captacao/:id/analise-edital"
          element={<AnaliseEditalPage />}
        />
        {/* Cotação */}
        <Route path="/cotacao" element={<CotacaoModulePage />} />

      </Route>

      <Route path="*" element={<LoginPage />} />
    </Routes>
  );
}
