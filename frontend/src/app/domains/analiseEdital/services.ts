import { api } from "@/app/infra/api";
import type { AnaliseEdital, AnaliseEditalCreateInput } from "./types";

export async function criarAnaliseEdital(
  data: AnaliseEditalCreateInput
): Promise<AnaliseEdital> {
  const response = await api.post("/analise-edital", data);
  return response.data;
}

export async function obterAnaliseEdital(
  analiseId: string
): Promise<AnaliseEdital> {
  const response = await api.get(`/analise-edital/${analiseId}`);
  return response.data;
}

export async function listarAnalisesPorOportunidade(
  oportunidadeId: string
): Promise<AnaliseEdital[]> {
  const response = await api.get(
    `/analise-edital/por-oportunidade/${oportunidadeId}`
  );
  return response.data;
}

// Evita duplicidade
export async function obterAnalisePorOportunidade(
  oportunidadeId: string
): Promise<AnaliseEdital | null> {
  const response = await api.get(
    `/analise-edital/por-oportunidade/${oportunidadeId}`
  );

  return response.data.length > 0 ? response.data[0] : null;
}