// Status do processo exatamente como o backend.
// Aqui é a fonte única — ninguém "inventa" status em módulos.

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
