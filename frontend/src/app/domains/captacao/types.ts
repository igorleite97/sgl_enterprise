// src/app/domains/captacao/types.ts
export type PortalCompras = "COMPRASNET" | "COMPRAS_PUBLICAS";

export interface CaptacaoInput {
  numero_processo: string;
  uasg: string;
  orgao: string;
  portal: PortalCompras;
  data_hora_disputa: string;
  itens: any[];
}

export type ItemCaptado = {
  id?: string; // gerado no backend
  numero_item: string;
  subgrupo: string;
  valor_referencia: number; 
  quantidade: number;
};

export type ProcessoCaptado = CaptacaoInput & {
  id: string;
  status: string;
  criado_em: string;
};

// Status do processo conforme backend
export type StatusProcesso =
  | "CAPTADO"
  | "ANALISE_EDITAL"
  | "COTACAO"
  | "DISPUTA"
  | "POS_PREGAO"
  | "CONTRATO"
  | "EMPENHO"
  | "ENCERRADO";
