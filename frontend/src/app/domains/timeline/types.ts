export type TipoEventoTimeline =
  | "CRIACAO"
  | "STATUS"
  | "DECISAO"
  | "OBSERVACAO";

export type SeveridadeEvento =
  | "BAIXA"
  | "MEDIA"
  | "ALTA"
  | "CRITICA";

export interface EventoTimeline {
  id: number;

  entidade_tipo: string;
  entidade_id: string;

  tipo: TipoEventoTimeline;
  severidade: SeveridadeEvento;

  titulo?: string;
  descricao: string;

  usuario?: string | null;

  criado_em: string; // ISO string vinda da API
}
