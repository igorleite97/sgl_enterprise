import { useEffect, useMemo, useState } from "react";
import { useSearchParams } from "react-router-dom";

import { obterCaptacaoPorId } from "@/app/domains/captacao/services";
import { obterAnalisePorOportunidade } from "@/app/domains/analiseEdital/services";

import type { ProcessoCotacaoView, AnaliseEditalResumo } from "@/app/domains/cotacao/types";
import { CotacaoPage } from "./CotacaoPage";

function toResumo(analise: any): AnaliseEditalResumo {
  return {
    prazo_entrega_dias: analise.prazo_entrega_dias,
    exige_amostra: analise.exige_amostra,
    permite_adesao: analise.permite_adesao,
    exige_garantia_proposta: analise.exige_garantia_proposta,
    local_entrega: analise.local_entrega,
    decisao: analise.decisao,
    motivo_desistencia: analise.motivo_desistencia,
  };
}

export function CotacaoPageContainer() {
  const [searchParams] = useSearchParams();
  const pid = useMemo(() => searchParams.get("pid"), [searchParams]);

  const [processo, setProcesso] = useState<ProcessoCotacaoView | null>(null);
  const [analiseResumo, setAnaliseResumo] = useState<AnaliseEditalResumo | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!pid) {
      setProcesso(null);
      setAnaliseResumo(null);
      return;
    }

    setLoading(true);

    Promise.all([
      obterCaptacaoPorId(pid),
      obterAnalisePorOportunidade(pid),
    ])
      .then(([cap, analise]) => {
        const mapped: ProcessoCotacaoView = {
          id: cap.id,
          numero: cap.numero_processo,
          orgao: cap.orgao,
          uasg: cap.uasg,
          status: cap.status,
          portal: cap.portal,
          data_hora_disputa: cap.data_hora_disputa,
          itens: (cap.itens ?? []).map((it: any, idx: number) => ({
            id: it.id ?? `${cap.id}-${idx}`,
            numero: Number(it.numero_item ?? idx + 1),
            descricao: it.descricao ?? it.subgrupo ?? "—",
            qtd: Number(it.quantidade ?? 1),
            un: it.unidade ?? "UN",
            estimado_unit: Number(it.valor_referencia ?? 0),
          })),
        };

        setProcesso(mapped);
        setAnaliseResumo(analise ? toResumo(analise) : null);
      })
      .finally(() => setLoading(false));
  }, [pid]);

  if (!pid) {
    return <div style={{ padding: 24 }}>Selecione um processo à esquerda para iniciar.</div>;
  }

  if (loading) {
    return <div style={{ padding: 24 }}>Carregando cotação…</div>;
  }

  if (!processo) {
    return <div style={{ padding: 24 }}>Processo não encontrado.</div>;
  }

  return <CotacaoPage processo={processo} analiseResumo={analiseResumo} />;
}
