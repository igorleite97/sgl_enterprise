import { Routes, Route, Navigate } from "react-router-dom";

import { LoginPage } from "@/app/pages/LoginPage";
import { DashboardPage } from "@/app/domains/dashboard/pages/DashboardPage";

import { CaptacaoPage } from "@/app/domains/captacao/pages/CaptacaoPage";
import { CaptacaoDetalhePage } from "@/app/domains/captacao/pages/CaptacaoDetalhePage";

import { AnaliseEditalListPage } from "@/app/domains/analiseEdital/pages/AnaliseEditalListPage";
import { AnaliseEditalPage } from "@/app//domains/analiseEdital/pages/AnaliseEditalPage";

import { CotacaoListPage } from "@/app/domains/cotacao/pages/CotacaoListPage";
import { CotacaoWorkspacePage } from "@/app/domains/cotacao/pages/CotacaoWorkspacePage";


import { ProtectedRoute } from "@/app/router/ProtectedRoute";
import { AppLayout } from "@/app/layout/AppLayout";

export function AppRouter() {
  return (
    <Routes>
      {/* público */}
      <Route path="/login" element={<LoginPage />} />

      {/* protegido */}
      <Route element={<ProtectedRoute />}>
        <Route element={<AppLayout />}>
          {/* default: manda para dashboard */}
          <Route index element={<Navigate to="/dashboard" replace />} />

          <Route path="dashboard" element={<DashboardPage />} />

          <Route path="captacao" element={<CaptacaoPage />} />
          <Route path="captacao/:id" element={<CaptacaoDetalhePage />} />

          <Route path="analise-edital" element={<AnaliseEditalListPage />} />
          <Route path="captacao/:id/analise-edital" element={<AnaliseEditalPage />}/>
          <Route path="cotacao" element={<CotacaoListPage />} />
          <Route path="/cotacao" element={<CotacaoWorkspacePage />} />
        </Route>
      </Route>

      {/* fallback */}
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  );
}
