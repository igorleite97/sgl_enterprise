import type { StatusProcesso } from "@/app/core/statusProcesso";
import type { AnaliseEdital } from "@/app/domains/analiseEdital/types";

export type { StatusProcesso };


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

/**
 * ViewModel específico da tela de Cotação.
 * Aqui eu deixo somente o que a UI realmente precisa.
 */

export type AnaliseEditalResumo = {
  prazo_entrega_dias: number;
  exige_amostra: boolean;
  permite_adesao: boolean;
  exige_garantia_proposta: boolean;
  local_entrega: string;
  decisao: "SEGUIR" | "DESISTIR";
  motivo_desistencia?: string;
};

export type ProcessoCotacaoView = {
  id: string;
  numero: string;
  orgao: string;
  uasg?: string;
  status: StatusProcesso;
  portal?: string;
  modalidade?: string;
  data_hora_disputa?: string;
  itens: Array<{
    id: string;
    numero: number;
    descricao: string;
    qtd: number;
    un: string;
    estimado_unit: number;
  }>;
};
