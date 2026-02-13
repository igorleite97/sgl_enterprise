import type { ProcessoCotacaoView, AnaliseEditalResumo } from "@/app/domains/cotacao/types";

type Props = {
  processo: ProcessoCotacaoView;
  analiseResumo: AnaliseEditalResumo | null;
};

export function CotacaoPage({ processo, analiseResumo }: Props) {
  return (
    <div>
      {/* Header do processo + um mini resumo da análise (colapsado por padrão) */}
      {/* ...seu JSX... */}
    </div>
  );
}
