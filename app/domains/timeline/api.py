from fastapi import APIRouter, Query
from typing import Optional, List

from app.db.memory import db
from app.domains.timeline.models import EventoTimeline
from app.domains.timeline.enums import TipoEventoTimeline, SeveridadeEvento

router = APIRouter(
    prefix="/timeline",
    tags=["Timeline"],
)


@router.get("/", response_model=List[EventoTimeline])
def listar_timeline(
    entidade: Optional[str] = Query(None),
    entidade_id: Optional[int] = Query(None),
    tipo_evento: Optional[TipoEventoTimeline] = Query(None),
    severidade: Optional[SeveridadeEvento] = Query(None),
    order: str = Query("desc", pattern="^(asc|desc)$"),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    eventos = db["timeline"]

    # 🔍 Filtros
    if entidade:
        eventos = [e for e in eventos if e.entidade_tipo == entidade]

    if entidade_id:
        eventos = [e for e in eventos if e.entidade_id == entidade_id]

    if tipo_evento:
        eventos = [e for e in eventos if e.tipo == tipo_evento]

    if severidade:
        eventos = [e for e in eventos if e.severidade == severidade]


    # ↕ Ordenação
    eventos = sorted(
        eventos,
        key=lambda e: e.criado_em,
        reverse=(order == "desc"),
    )

    # 📄 Paginação
    return eventos[offset : offset + limit]

