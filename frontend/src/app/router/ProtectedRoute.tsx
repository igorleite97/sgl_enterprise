// src/app/router/AppRouter.tsx
import { Routes, Route } from "react-router-dom";

import { ProtectedRoute } from "@/app/router/ProtectedRoute";
import { AppLayout } from "@/app/layout/AppLayout";

import { DashboardPage } from "@/app/domains/dashboard/pages/DashboardPage";
import { CaptacaoPage } from "@/app/domains/captacao/pages/CaptacaoPage";
import { CaptacaoDetalhePage } from "@/app/domains/captacao/pages/CaptacaoDetalhePage";

import { EditalListPage } from "@/app/domains/analiseEdital/pages/EditalListPage";
import { CotacaoListPage } from "@/app/domains/cotacao/pages/CotacaoListPage";

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
        <Route path="/" element={<DashboardPage />} />

        <Route path="/captacao" element={<CaptacaoPage />} />
        <Route path="/captacao/:id" element={<CaptacaoDetalhePage />} />

        <Route path="/editais" element={<EditalListPage />} />
        <Route path="/cotacao" element={<CotacaoListPage />} />

        {/* demais módulos depois */}
      </Route>
    </Routes>
  );
}
