from app.db.memory import db, now
from app.domains.timeline.models import EventoTimeline
from app.domains.timeline.enums import TipoEventoTimeline, SeveridadeEvento
from app.domains.timeline.rules import resolver_severidade


def registrar_evento_timeline(
    entidade: str,
    entidade_id: str | int,
    tipo_evento: TipoEventoTimeline,
    descricao: str,
    severidade: SeveridadeEvento | None = None,
    usuario: str | None = None,
) -> EventoTimeline:

    severidade_final = severidade or resolver_severidade(tipo_evento)

    evento = EventoTimeline(
        id=len(db["timeline"]) + 1,
        entidade=entidade,
        entidade_id=entidade_id,
        tipo_evento=tipo_evento,
        descricao=descricao,
        severidade=severidade_final,
        usuario=usuario,
        criado_em=now(),
    )

    db["timeline"].append(evento)
    return evento
