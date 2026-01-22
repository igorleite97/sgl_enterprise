import type {
  CaptacaoInput,
  ProcessoCaptado,
  StatusProcesso,
} from "./types";

import { api } from "@/app/infra/api";

export async function registrarCaptacao(
  payload: CaptacaoInput
): Promise<ProcessoCaptado> {
  const response = await api.post("/captacao", payload);
  return response.data;
}

export async function listarCaptacoes(): Promise<ProcessoCaptado[]> {
  const response = await api.get("/captacao");
  return response.data;
}

export async function alterarStatusCaptacao(
  captacaoId: string,
  novoStatus: StatusProcesso,
  justificativa?: string
) {
  return api.patch(`/captacao/${captacaoId}/status`, {
    status: novoStatus,
    justificativa,
  });
}
