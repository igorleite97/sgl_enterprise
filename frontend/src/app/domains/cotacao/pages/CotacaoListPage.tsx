import { useEffect, useMemo, useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";

import { listarCaptacoes } from "@/app/domains/captacao/services";
import type { ProcessoCaptado } from "@/app/domains/captacao/types";
import type { StatusProcesso } from "@/app/core/statusProcesso";

import { ProcessoCard } from "@/app/domains/cotacao/components/ProcessoCard";

// A cotação só deve “enxergar” processos que já passaram pelo filtro objetivo da Análise de Edital.
// Se no seu fluxo o status “apto” for outro, você ajusta aqui e pronto.
const STATUS_APTOS_PARA_COTACAO: StatusProcesso[] = ["ANALISE_APROVADA"];

export function CotacaoListPage() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  const [processos, setProcessos] = useState<ProcessoCaptado[]>([]);
  const [loading, setLoading] = useState(true);
  const [q, setQ] = useState("");

  // Se já tiver pid na URL, eu uso isso pra destacar o card (fica bem “SPA”)
  const pidSelecionado = searchParams.get("pid");

  useEffect(() => {
    setLoading(true);

    listarCaptacoes()
      .then(setProcessos)
      .finally(() => setLoading(false));
  }, []);

  const aptos = useMemo(() => {
    const base = processos.filter((p) =>
      STATUS_APTOS_PARA_COTACAO.includes(p.status)
    );

    const term = q.trim().toLowerCase();
    if (!term) return base;

    return base.filter((p) => {
      const alvo = [
        p.numero_processo,
        p.uasg,
        p.orgao,
        p.portal,
        p.data_hora_disputa,
      ]
        .filter(Boolean)
        .join(" ")
        .toLowerCase();

      return alvo.includes(term);
    });
  }, [processos, q]);

  function abrirCotacao(processoId: string) {
    // Eu mantenho a rota do módulo e só troco o “contexto” via query param.
    navigate(`/cotacao?pid=${processoId}`);
  }

  if (loading) {
    return <div style={{ padding: 24 }}>Carregando processos aptos para cotação…</div>;
  }

  return (
    <div style={{ padding: 24 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end", gap: 12 }}>
        <div>
          <h1 style={{ margin: 0 }}>Cotação</h1>
          <div style={{ color: "#0048d8", fontSize: 13, marginTop: 6 }}>
            Selecione um processo apto para iniciar a cotação.
          </div>
        </div>

        <div style={{ color: "#6b7280", fontSize: 13 }}>
          {aptos.length} processo(s) apto(s)
        </div>
      </div>

      <input
        value={q}
        onChange={(e) => setQ(e.target.value)}
        placeholder="Buscar por processo, UASG, órgão, portal ou data..."
        style={{
          width: "100%",
          padding: "10px 12px",
          border: "1px solid #e5e7eb",
          borderRadius: 10,
          marginTop: 14,
          marginBottom: 12,
        }}
      />

      {aptos.length === 0 ? (
        <div
          style={{
            border: "1px dashed #d1d5db",
            padding: 16,
            borderRadius: 12,
            color: "#6b7280",
          }}
        >
          Nenhum processo disponível para cotação no momento.
        </div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          {aptos.map((p) => (
            <ProcessoCard
              key={p.id}
              numero_processo={p.numero_processo}
              uasg={p.uasg}
              orgao={p.orgao}
              portal={p.portal}
              // Se ainda não existir no backend, deixa como "—" por enquanto.
              modalidade={(p as any).modalidade}
              data_hora_disputa={p.data_hora_disputa}
              status={p.status}
              itensCount={p.itens?.length ?? 0}
              selecionado={pidSelecionado === p.id}
              onClick={() => abrirCotacao(p.id)}
            />
          ))}
        </div>
      )}
    </div>
  );
}
