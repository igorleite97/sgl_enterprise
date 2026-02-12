import { useEffect, useMemo, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { CotacaoPage } from "./CotacaoPage";

// TODO: troque pelos seus serviços reais
import { obterCaptacaoPorId } from "@/app/domains/captacao/services";
import { listarCotacoesPorOportunidade } from "@/app/domains/cotacao/services";

type ProcessoCotacao = {
  id: string;
  numero: string;
  orgao: string;
  uasg?: string;
  status: "EM_COTACAO" | "PENDENTE";
  itens: Array<{
    id: string;
    numero: number;
    descricao: string;
    qtd: number;
    un: string;
    estimado_unit: number;
  }>;
};

export function CotacaoPageContainer() {
  const [searchParams] = useSearchParams();
  const pid = useMemo(() => searchParams.get("pid"), [searchParams]);

  const [processo, setProcesso] = useState<ProcessoCotacao | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!pid) {
      setProcesso(null);
      return;
    }

    setLoading(true);

    Promise.all([
      obterCaptacaoPorId(pid), // ou obterOportunidade(pid)
      listarCotacoesPorOportunidade(pid), // se já existir
    ])
      .then(([cap, cotacoes]) => {
        // Monte o shape que sua CotacaoPage espera
        const mapped: ProcessoCotacao = {
          id: cap.id,
          numero: cap.numero_processo,
          orgao: cap.orgao,
          uasg: cap.uasg,
          status: "EM_COTACAO", // ou derive do cap.status
          itens: cap.itens.map((it: any, idx: number) => ({
            id: it.id ?? `${cap.id}-${idx}`,
            numero: Number(it.numero_item ?? idx + 1),
            descricao: it.descricao ?? it.subgrupo ?? "—",
            qtd: Number(it.quantidade ?? 1),
            un: it.unidade ?? "UN",
            estimado_unit: Number(it.valor_referencia ?? 0),
          })),
        };

        setProcesso(mapped);
      })
      .finally(() => setLoading(false));
  }, [pid]);

  if (!pid) return <div style={{ padding: 24 }}>Selecione um processo para iniciar a cotação.</div>;
  if (loading) return <div style={{ padding: 24 }}>Carregando cotação…</div>;
  if (!processo) return <div style={{ padding: 24 }}>Processo não encontrado.</div>;

  return <CotacaoPage processo={processo} />;
}
