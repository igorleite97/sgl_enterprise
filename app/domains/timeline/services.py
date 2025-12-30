from app.db.memory import db, now
from app.domains.timeline.models import EventoTimeline
from app.domains.timeline.enums import TipoEventoTimeline, OrigemEvento


def registrar_evento(
    entidade: str,
    entidade_id: int,
    tipo_evento: TipoEventoTimeline,
    descricao: str,
    origem: OrigemEvento = OrigemEvento.SISTEMA,
    usuario: str | None = None,
) -> EventoTimeline:
    evento = EventoTimeline(
        id=len(db["timeline"]) + 1,
        entidade=entidade,
        entidade_id=entidade_id,
        tipo_evento=tipo_evento,
        descricao=descricao,
        origem=origem,
        usuario=usuario,
        criado_em=now(),
    )

    db["timeline"].append(evento)
    return evento
