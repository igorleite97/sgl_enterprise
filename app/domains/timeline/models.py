from dataclasses import dataclass
from datetime import datetime
from app.domains.timeline.enums import TipoEventoTimeline, SeveridadeEvento

@dataclass
class EventoTimeline:
    id: int
    entidade_tipo: str
    entidade_id: str | int

    tipo_evento: TipoEventoTimeline
    severidade: SeveridadeEvento

    descricao: str
    usuario: str | None
    criado_em: datetime
