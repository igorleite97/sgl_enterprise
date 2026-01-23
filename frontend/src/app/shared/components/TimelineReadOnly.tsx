import type { EventoTimeline } from "@/app/domains/timeline/types";

type TimelineReadOnlyProps = {
  eventos: EventoTimeline[];
};

export function TimelineReadOnly({ eventos }: TimelineReadOnlyProps) {
  if (!eventos || eventos.length === 0) {
    return <p>Nenhum evento registrado.</p>;
  }

  const eventosOrdenados = [...eventos].sort(
    (a, b) =>
      new Date(b.criado_em).getTime() -
      new Date(a.criado_em).getTime()
  );

  return (
    <ul>
      {eventosOrdenados.map((evento) => (
        <li key={evento.id}>
          <strong>
            {new Date(evento.criado_em).toLocaleString()}
          </strong>
          <br />

          {evento.descricao}
          <br />

          <small>
            {evento.tipo} — {evento.severidade}
            {evento.usuario ? ` — ${evento.usuario}` : ""}
          </small>
        </li>
      ))}
    </ul>
  );
}
