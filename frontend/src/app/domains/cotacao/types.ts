// src/app/domains/cotacao/types.ts
import type { StatusProcesso } from "@/app/domains/captacao/types";

export type CotacaoCreateInput = {
  oportunidade_id: string;
  fornecedor: string;
  valor_total: number;
  prazo_entrega_dias: number;
  observacoes?: string | null;
};

export type Cotacao = {
  id: string;
  oportunidade_id: string;
  fornecedor: string;
  valor_total: number;
  prazo_entrega_dias: number;
  observacoes?: string | null;
  status: StatusProcesso;
  criado_em: string;
  atualizada_em?: string | null;
};
