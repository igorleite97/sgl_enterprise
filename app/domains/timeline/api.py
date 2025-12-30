from fastapi import APIRouter, Query
from typing import Optional, List

from app.db.memory import db
from app.domains.timeline.models import EventoTimeline
from app.domains.timeline.enums import TipoEventoTimeline, OrigemEvento

router = APIRouter(
    prefix="/timeline",
    tags=["Timeline"],
)


@router.get("/", response_model=List[EventoTimeline])
def listar_timeline(
    entidade: Optional[str] = Query(None),
    entidade_id: Optional[int] = Query(None),
    tipo_evento: Optional[TipoEventoTimeline] = Query(None),
    origem: Optional[OrigemEvento] = Query(None),
    order: str = Query("desc", regex="^(asc|desc)$"),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    eventos = db["timeline"]

    # 🔍 Filtros
    if entidade:
        eventos = [e for e in eventos if e.entidade == entidade]

    if entidade_id:
        eventos = [e for e in eventos if e.entidade_id == entidade_id]

    if tipo_evento:
        eventos = [e for e in eventos if e.tipo_evento == tipo_evento]

    if origem:
        eventos = [e for e in eventos if e.origem == origem]

    # ↕ Ordenação
    eventos = sorted(
        eventos,
        key=lambda e: e.criado_em,
        reverse=(order == "desc"),
    )

    # 📄 Paginação
    return eventos[offset : offset + limit]
