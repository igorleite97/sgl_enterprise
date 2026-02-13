import type { StatusProcesso } from "@/app/core/statusProcesso";

export const STATUS_LABEL: Partial<Record<StatusProcesso, string>> = {
  CAPTACAO: "Captação",
  ANALISE_EDITAL: "Análise de Edital",
  ANALISE_APROVADA: "Análise Aprovada",
  DESISTENCIA: "Desistência",
  COTACAO: "Cotação",
  COTACAO_INICIADA: "Cotação Iniciada",
  COTACAO_ENCERRADA: "Cotação Encerrada",
  DISPUTA: "Disputa",
  POS_PREGAO: "Pós-Pregão",
  CONTRATO: "Contrato",
};
