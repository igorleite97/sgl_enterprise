from dataclasses import dataclass
from datetime import datetime
from app.domains.timeline.enums import TipoEventoTimeline, OrigemEvento


@dataclass
class EventoTimeline:
    id: int
    entidade: str            # ex: "DISPUTA_ITEM", "LANCE", "POS_PREGAO"
    entidade_id: int
    tipo_evento: TipoEventoTimeline
    descricao: str

    origem: OrigemEvento
    usuario: str | None      # nome ou id do usuário

    criado_em: datetime
