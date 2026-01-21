import type {
  CaptacaoInput,
  ProcessoCaptado,
  StatusProcesso,
} from "./models";

import { api } from "../../infra/api";

export async function registrarCaptacao(
  data: CaptacaoInput
): Promise<ProcessoCaptado> {
  const response = await api.post("/captacao", data);
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
