// src/app/domains/analiseEdital/services.ts

import { api } from "@/app/infra/api";
import type { AnaliseEdital, AnaliseEditalCreate } from "./types";

export async function criarAnaliseEdital(
  payload: AnaliseEditalCreate
): Promise<AnaliseEdital> {
  const response = await api.post("/analise-edital", payload);
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
