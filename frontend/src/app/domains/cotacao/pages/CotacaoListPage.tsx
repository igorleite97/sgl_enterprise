// src/app/domains/cotacao/pages/CotacaoListPage.tsx
import { useEffect, useMemo, useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";

import { listarCaptacoes } from "@/app/domains/captacao/services";
import type { ProcessoCaptado } from "@/app/domains/captacao/types";

import { criarCotacao, listarCotacoesPorOportunidade } from "../services";
import type { Cotacao } from "../types";

export function CotacaoListPage() {
  const [params] = useSearchParams();
  const navigate = useNavigate();
  const pid = params.get("pid") ?? "";

  const [processos, setProcessos] = useState<ProcessoCaptado[]>([]);
  const [loadingProcessos, setLoadingProcessos] = useState(true);

  const [cotacoes, setCotacoes] = useState<Cotacao[]>([]);
  const [loadingCotacoes, setLoadingCotacoes] = useState(false);

  // form
  const [fornecedor, setFornecedor] = useState("");
  const [valorTotal, setValorTotal] = useState<number>(0);
  const [prazoEntrega, setPrazoEntrega] = useState<number>(0);
  const [observacoes, setObservacoes] = useState("");

  useEffect(() => {
    setLoadingProcessos(true);
    listarCaptacoes()
      .then(setProcessos)
      .finally(() => setLoadingProcessos(false));
  }, []);

  const processosAptos = useMemo(() => {
    // enquanto o backend estiver exigindo ANALISE_EDITAL, a gente aceita os dois no front
    const allowed = new Set(["ANALISE_APROVADA", "ANALISE_EDITAL"]);
    return processos.filter((p) => allowed.has(p.status));
  }, [processos]);

  const processoSelecionado = useMemo(
    () => processosAptos.find((p) => p.id === pid) ?? null,
    [processosAptos, pid]
  );

  useEffect(() => {
    if (!pid) {
      setCotacoes([]);
      return;
    }
    setLoadingCotacoes(true);
    listarCotacoesPorOportunidade(pid)
      .then(setCotacoes)
      .finally(() => setLoadingCotacoes(false));
  }, [pid]);

  function selecionarProcesso(id: string) {
    navigate({ pathname: "/cotacao", search: `?pid=${id}` });
  }

  async function handleCriarCotacao() {
    if (!pid) return;

    if (!fornecedor.trim()) return alert("Informe o fornecedor");
    if (valorTotal <= 0) return alert("Valor total deve ser maior que zero");
    if (prazoEntrega <= 0) return alert("Prazo deve ser maior que zero");

    const nova = await criarCotacao({
      oportunidade_id: pid,
      fornecedor,
      valor_total: valorTotal,
      prazo_entrega_dias: prazoEntrega,
      observacoes: observacoes || null,
    });

    // refresha listagem
    setCotacoes((prev) => [nova, ...prev]);

    // reset form
    setFornecedor("");
    setValorTotal(0);
    setPrazoEntrega(0);
    setObservacoes("");
  }

  return (
    <div style={{ display: "flex", gap: 16, height: "calc(100vh - 64px)" }}>
      {/* ESQUERDA */}
      <section style={{ width: 340, borderRight: "1px solid #e5e7eb", paddingRight: 16, overflow: "auto" }}>
        <h1 style={{ fontSize: 18, marginBottom: 8 }}>Cotação</h1>
        <p style={{ color: "#6b7280", marginBottom: 16 }}>
          Selecione um processo apto para cotação.
        </p>

        {loadingProcessos && <p>Carregando processos...</p>}

        {!loadingProcessos && processosAptos.length === 0 && (
          <p style={{ color: "#6b7280" }}>Nenhum processo disponível para cotação.</p>
        )}

        <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
          {processosAptos.map((p) => {
            const active = p.id === pid;
            return (
              <button
                key={p.id}
                onClick={() => selecionarProcesso(p.id)}
                style={{
                  textAlign: "left",
                  padding: 12,
                  borderRadius: 10,
                  border: "1px solid #e5e7eb",
                  background: active ? "#eef2ff" : "#fff",
                  cursor: "pointer",
                }}
              >
                <div style={{ fontWeight: 700 }}>{p.numero_processo}</div>
                <div style={{ fontSize: 12, color: "#6b7280" }}>
                  {p.orgao} · {p.uasg} · Status: {p.status}
                </div>
              </button>
            );
          })}
        </div>
      </section>

      {/* DIREITA */}
      <section style={{ flex: 1, overflow: "auto" }}>
        {!processoSelecionado && (
          <div style={{ padding: 24, color: "#6b7280" }}>
            Selecione um processo à esquerda para iniciar.
          </div>
        )}

        {processoSelecionado && (
          <div style={{ padding: 24 }}>
            <h2 style={{ fontSize: 20, marginBottom: 8 }}>
              {processoSelecionado.numero_processo}
            </h2>

            <div style={{ color: "#6b7280", marginBottom: 16 }}>
              {processoSelecionado.orgao} · UASG {processoSelecionado.uasg} · Portal {processoSelecionado.portal}
            </div>

            <div style={{ display: "flex", gap: 16, alignItems: "flex-start" }}>
              {/* TABELA */}
              <div style={{ flex: 1 }}>
                <h3 style={{ marginBottom: 8 }}>Cotações registradas</h3>

                {loadingCotacoes && <p>Carregando cotações...</p>}

                {!loadingCotacoes && cotacoes.length === 0 && (
                  <p style={{ color: "#6b7280" }}>Nenhuma cotação registrada ainda.</p>
                )}

                {cotacoes.length > 0 && (
                  <table width="100%" cellPadding={10} style={{ borderCollapse: "collapse" }}>
                    <thead>
                      <tr style={{ textAlign: "left", borderBottom: "1px solid #e5e7eb" }}>
                        <th>Fornecedor</th>
                        <th>Valor Total</th>
                        <th>Prazo (dias)</th>
                        <th>Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      {cotacoes.map((c) => (
                        <tr key={c.id} style={{ borderBottom: "1px solid #f3f4f6" }}>
                          <td>{c.fornecedor}</td>
                          <td>
                            {c.valor_total.toLocaleString("pt-BR", {
                              style: "currency",
                              currency: "BRL",
                            })}
                          </td>
                          <td>{c.prazo_entrega_dias}</td>
                          <td>{c.status}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                )}
              </div>

              {/* FORM */}
              <div style={{ width: 360, border: "1px solid #e5e7eb", borderRadius: 12, padding: 16 }}>
                <h3 style={{ marginBottom: 12 }}>Registrar cotação</h3>

                <input
                  placeholder="Fornecedor"
                  value={fornecedor}
                  onChange={(e) => setFornecedor(e.target.value)}
                  style={{ width: "100%", marginBottom: 8 }}
                />

                <input
                  type="number"
                  placeholder="Valor total"
                  value={valorTotal || ""}
                  onChange={(e) => setValorTotal(Number(e.target.value))}
                  style={{ width: "100%", marginBottom: 8 }}
                />

                <input
                  type="number"
                  placeholder="Prazo de entrega (dias)"
                  value={prazoEntrega || ""}
                  onChange={(e) => setPrazoEntrega(Number(e.target.value))}
                  style={{ width: "100%", marginBottom: 8 }}
                />

                <textarea
                  placeholder="Observações"
                  value={observacoes}
                  onChange={(e) => setObservacoes(e.target.value)}
                  style={{ width: "100%", marginBottom: 12 }}
                />

                <button onClick={handleCriarCotacao} style={{ width: "100%" }}>
                  Salvar Cotação
                </button>
              </div>
            </div>
          </div>
        )}
      </section>
    </div>
  );
}
