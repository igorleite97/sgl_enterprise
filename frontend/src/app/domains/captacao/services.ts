import type {
  CaptacaoInput,
  ProcessoCaptado,
  StatusProcesso,
  EventoTimeline,
} from "./types";

import { api } from "@/app/infra/api";
import axios from "axios";

export async function registrarCaptacao(payload: CaptacaoInput) {
  try {
    const response = await api.post("/captacao", payload);
    return response.data;
  } catch (error: any) {
    if (axios.isAxiosError(error) && error.response?.status === 409) {
      const detail = error.response.data.detail;

      throw {
        tipo: detail.tipo,
        mensagem: detail.mensagem,
        processoId: detail.processoId,
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

export async function obterCaptacaoPorId(
  captacaoId: string
): Promise<ProcessoCaptado> {
  const response = await api.get<ProcessoCaptado>(
    `/captacao/${captacaoId}`
  );

  return response.data;
}

export async function obterTimelineCaptacao(
  captacaoId: string
): Promise<EventoTimeline[]> {
  const response = await api.get(
    `/timeline/captacao/${captacaoId}`
  );
  return response.data;
}