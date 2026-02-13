import { useEffect, useMemo, useState } from "react";
import { useSearchParams } from "react-router-dom";

import { CotacaoPageContainer } from "./CotacaoPageContainer";
import { STATUS_LABEL } from "@/app/domains/cotacao/status";

import { listarCaptacoes } from "@/app/domains/captacao/services";
import type { ProcessoCaptado } from "@/app/domains/captacao/types";

function toISODate(date: Date) {
  // YYYY-MM-DD (bom pra filtro por dia)
  return date.toISOString().slice(0, 10);
}

export function CotacaoWorkspacePage() {
  const [searchParams, setSearchParams] = useSearchParams();
  const pid = searchParams.get("pid");

  const [loading, setLoading] = useState(false);
  const [processos, setProcessos] = useState<ProcessoCaptado[]>([]);

  // filtros simples (primeira versão: objetiva e útil)
  const [q, setQ] = useState("");
  const [dia, setDia] = useState(() => toISODate(new Date()));

  useEffect(() => {
    let cancelled = false;

    async function load() {
      setLoading(true);
      try {
        const all = await listarCaptacoes();

        if (cancelled) return;

        /**
         * Regra de negócio do front:
         * Só aparece na fila quem está apto a entrar em Cotação.
         *
         * Observação importante:
         * - Se o backend liberar "ANALISE_APROVADA" e/ou "ANALISE_EDITAL", ajuste aqui.
         * - Eu deixo essa regra explícita no front pra evitar "cotação vazia" sem explicação.
         */
        const aptos = all.filter((p) => p.status === "ANALISE_EDITAL" || p.status === "ANALISE_APROVADA");
        setProcessos(aptos);
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    load();
    return () => {
      cancelled = true;
    };
  }, []);

  const filtrados = useMemo(() => {
    const term = q.trim().toLowerCase();

    return processos.filter((p) => {
      const bateTexto =
        !term ||
        p.numero_processo.toLowerCase().includes(term) ||
        p.orgao.toLowerCase().includes(term) ||
        p.uasg.toLowerCase().includes(term);

      const bateDia =
        !dia || (p.data_hora_disputa ? p.data_hora_disputa.slice(0, 10) === dia : true);

      return bateTexto && bateDia;
    });
  }, [processos, q, dia]);

  const kpiTotal = filtrados.length;

  function selecionar(processoId: string) {
    // Eu faço isso porque mantém o back/forward do navegador funcionando bem.
    setSearchParams((prev) => {
      const next = new URLSearchParams(prev);
      next.set("pid", processoId);
      return next;
    });
  }

  return (
    <div style={{ display: "grid", gridTemplateColumns: "360px 1fr", gap: 16, padding: 24 }}>
      {/* COLUNA ESQUERDA: FILA */}
      <aside style={{ border: "1px solid #e5e7eb", borderRadius: 12, padding: 12 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginBottom: 10 }}>
          <div>
            <h2 style={{ margin: 0 }}>Fila de Cotação</h2>
            <div style={{ fontSize: 12, color: "#6b7280" }}>
              {loading ? "Carregando…" : `${kpiTotal} processo(s) apto(s)`}
            </div>
          </div>
        </div>

        <div style={{ display: "grid", gap: 8, marginBottom: 12 }}>
          <input
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="Buscar por processo, UASG ou órgão…"
            style={{ padding: "10px 12px", borderRadius: 10, border: "1px solid #e5e7eb" }}
          />

          <input
            type="date"
            value={dia}
            onChange={(e) => setDia(e.target.value)}
            style={{ padding: "10px 12px", borderRadius: 10, border: "1px solid #e5e7eb" }}
          />
        </div>

        <div style={{ display: "grid", gap: 10 }}>
          {filtrados.length === 0 ? (
            <div style={{ color: "#6b7280", fontSize: 13, padding: 10 }}>
              Nenhum processo disponível com esses filtros.
            </div>
          ) : (
            filtrados.map((p) => {
              const ativo = pid === p.id;

              return (
                <button
                  key={p.id}
                  onClick={() => selecionar(p.id)}
                  style={{
                    textAlign: "left",
                    padding: 12,
                    borderRadius: 12,
                    border: "1px solid #e5e7eb",
                    background: ativo ? "#eff6ff" : "#fff",
                    cursor: "pointer",
                  }}
                >
                  <div style={{ fontWeight: 800 }}>{p.numero_processo}</div>
                  <div style={{ fontSize: 13, color: "#374151" }}>{p.orgao}</div>
                  <div style={{ fontSize: 12, color: "#6b7280", marginTop: 4 }}>
                    UASG {p.uasg} • {STATUS_LABEL[p.status]}
                  </div>
                </button>
              );
            })
          )}
        </div>
      </aside>

      {/* PAINEL PRINCIPAL: DETALHE */}
      <main style={{ border: "1px solid #e5e7eb", borderRadius: 12, padding: 16 }}>
        {!pid ? (
          <div style={{ color: "#6b7280" }}>
            Selecione um processo na fila ao lado para iniciar a cotação.
          </div>
        ) : (
          <CotacaoPageContainer pid={pid} />
        )}
      </main>
    </div>
  );
}
