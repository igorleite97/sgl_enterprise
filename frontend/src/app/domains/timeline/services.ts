
import { api } from "@/app/infra/api";
import type { EventoTimeline } from "./types";

export async function obterTimelineCaptacao(
  captacaoId: string
): Promise<EventoTimeline[]> {
  const response = await api.get(
    `/timeline/CAPTACAO/${captacaoId}`
  );
  return response.data;
}