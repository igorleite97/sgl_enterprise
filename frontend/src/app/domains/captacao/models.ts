// Espelha app.domains.captacao.models

export type StatusProcesso =
  | "IDENTIFICADA"
  | "EM_ANALISE"
  | "COTACAO"
  | "DISPUTA"
  | "POS_PREGAO"
  | "CONTRATO"
  | "ENCERRADO";

export interface CaptacaoItem {
  descricao: string;
  quantidade: number;
  unidade: string;
}

export interface CaptacaoInput {
  numero_processo: string;
  uasg: string;
  orgao: string;
  portal: string;
  data_hora_disputa: string;
  itens: CaptacaoItem[];
}

export interface ProcessoCaptado {
  id: string;
  numero_processo: string;
  uasg: string;
  orgao: string;
  portal: string;
  data_hora_disputa: string;
  status: StatusProcesso;
  criado_em: string;
  atualizada_em?: string;
  itens: CaptacaoItem[];
}
