from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.domains.disputa.services import (
    iniciar_disputa,
    encerrar_disputa_item,
)
from app.db.memory import db
from app.core.enums import PerfilUsuario
from app.domains.disputa.services import registrar_lance

router = APIRouter(
    prefix="/disputa",
    tags=["Disputa"],
)

# =========================
# Schemas
# =========================

class IniciarDisputaRequest(BaseModel):
    oportunidade_id: int


class RegistrarLanceRequest(BaseModel):
    disputa_item_id: int
    preco_unitario: float
    quantidade: int
    markup_real: float
    posicao_final: int
    lance_vencedor: Optional[float] = None
    perfil_usuario: PerfilUsuario


class EncerrarDisputaItemRequest(BaseModel):
    disputa_item_id: int
    posicao_final: int

class ConsolidarDisputaRequest(BaseModel):
    oportunidade_id: str

# =========================
# Endpoints
# =========================

@router.post("/iniciar")
def api_iniciar_disputa(payload: IniciarDisputaRequest):
    return iniciar_disputa(payload.oportunidade_id)


@router.post("/lance")
def api_registrar_lance(payload: RegistrarLanceRequest):
    return registrar_lance(**payload.dict())


@router.post("/encerrar-item")
def api_encerrar_disputa_item(payload: EncerrarDisputaItemRequest):
    disputa_item = next(
        (i for i in db["disputa_itens"] if i.id == payload.disputa_item_id),
        None,
    )

    if not disputa_item:
        raise HTTPException(status_code=404, detail="Item de disputa não encontrado.")

    return encerrar_disputa_item(
        disputa_item=disputa_item,
        posicao_final=payload.posicao_final,
    )
