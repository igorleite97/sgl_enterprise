// src/app/domains/captacao/types.ts
export type PortalCompras = "COMPRASNET" | "COMPRAS_PUBLICAS";

export interface CaptacaoInput {
  numero_processo: string;
  uasg: string;
  orgao: string;
  portal: PortalCompras;
  data_hora_disputa: string;
  itens: ItemCaptado[];
}

export type ItemCaptado = {
  id?: string; // gerado no backend
  numero_item: string;
  subgrupo: string;
  valor_referencia: number | null;
  quantidade: number;
};

export type ProcessoCaptado = CaptacaoInput & {
  id: string;
  status: StatusProcesso;
  criado_em: string;
};

export type EventoTimeline = {
  id: string;
  data_hora: string;
  tipo_evento: string;
  descricao: string;
  severidade: "INFO" | "ALERTA" | "CRITICO"
  usuario: string;

};


// Status do processo conforme Backend
export type StatusProcesso =
  | "CAPTACAO"
  | "ANALISE_EDITAL"
  | "ANALISE_APROVADA"
  | "DESISTENCIA"
  | "COTACAO"
  | "COTACAO_INICIADA"
  | "COTACAO_ENCERRADA"
  | "DISPUTA"
  | "POS_PREGAO"
  | "CONTRATO";

