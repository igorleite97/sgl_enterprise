from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.db.memory import db
from app.domains.pos_pregao.services import (
    iniciar_pos_pregao,
    avancar_status,
    encerrar_pos_pregao,
)
from app.domains.pos_pregao.enums import StatusPosPregao


router = APIRouter(prefix="/pos-pregao", tags=["Pós-Pregão"])


class AvancarStatusRequest(BaseModel):
    pos_pregao_id: int
    novo_status: StatusPosPregao


@router.post("/iniciar/{disputa_item_id}")
def api_iniciar_pos_pregao(disputa_item_id: int):
    disputa_item = next(
        (i for i in db["disputa_itens"] if i.id == disputa_item_id),
        None,
    )

    if not disputa_item:
        raise HTTPException(status_code=404, detail="Item de disputa não encontrado.")

    return iniciar_pos_pregao(disputa_item)


@router.post("/avancar-status")
def api_avancar_status(payload: AvancarStatusRequest):
    pos = next(
        (p for p in db["pos_pregao_itens"] if p.id == payload.pos_pregao_id),
        None,
    )

    if not pos:
        raise HTTPException(status_code=404, detail="Pós-pregão não encontrado.")

    avancar_status(pos, payload.novo_status)
    return pos


@router.post("/encerrar/{pos_pregao_id}")
def api_encerrar_pos_pregao(pos_pregao_id: int):
    pos = next(
        (p for p in db["pos_pregao_itens"] if p.id == pos_pregao_id),
        None,
    )

    if not pos:
        raise HTTPException(status_code=404, detail="Pós-pregão não encontrado.")

    encerrar_pos_pregao(pos)
    return pos
