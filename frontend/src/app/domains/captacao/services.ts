import type {
  CaptacaoInput,
  ProcessoCaptado,
  StatusProcesso,
} from "./types";

import { api } from "@/app/infra/api";
import axios from "axios";

export async function registrarCaptacao(payload: CaptacaoInput) {
  try {
    const response = await api.post("/captacao", payload);
    return response.data;
  } catch (error: any) {
    if (axios.isAxiosError(error) && error.response?.status === 409) {
      throw {
        tipo: "CAPTACAO_DUPLICADA",
        processoId: error.response.data.processo_id,
        mensagem: error.response.data.message,
      };
    }

    throw error;
  }
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
