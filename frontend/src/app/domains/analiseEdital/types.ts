// src/app/domains/analiseEdital/types.ts

export type DecisaoAnaliseEdital = "SEGUIR" | "DESISTIR";

export interface AnaliseEditalCreate {
  oportunidade_id: string;

  prazo_entrega_dias: number;
  exige_amostra: boolean;
  permite_adesao: boolean;
  exige_garantia_proposta: boolean;

  local_entrega: string;
  observacoes?: string;

  decisao: DecisaoAnaliseEdital;
  motivo_desistencia?: string;
}

export interface AnaliseEdital extends AnaliseEditalCreate {
  id: string;
  criado_em: string;
}
