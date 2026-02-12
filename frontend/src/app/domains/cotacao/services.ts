import { api } from "@/app/infra/api";
import type { Cotacao, CotacaoCreateInput } from "./types";

export async function listarCotacoesPorOportunidade(oportunidadeId: string): Promise<Cotacao[]> {
  const res = await api.get<Cotacao[]>(`/cotacoes/oportunidade/${oportunidadeId}`);
  return res.data;
}

export async function criarCotacao(payload: CotacaoCreateInput): Promise<Cotacao> {
  const res = await api.post<Cotacao>("/cotacoes/", payload);
  return res.data;
}

export async function obterCotacao(cotacaoId: string): Promise<Cotacao> {
  const res = await api.get<Cotacao>(`/cotacoes/${cotacaoId}`);
  return res.data;
}
