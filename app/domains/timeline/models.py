from dataclasses import dataclass
from datetime import datetime
from app.domains.timeline.enums import TipoEventoTimeline, SeveridadeEvento

@dataclass
class EventoTimeline:
    id: int

    tipo: TipoEventoTimeline
    severidade: SeveridadeEvento

    entidade_id: str
    entidade_tipo: str

    titulo: str
    descricao: str

    usuario: str | None
    criado_em: datetime
