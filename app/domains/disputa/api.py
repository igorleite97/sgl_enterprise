from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.domains.disputa.services import (
    iniciar_disputa,
    registrar_lance,
    encerrar_disputa_item,
)
from app.domains.disputa.models import DisputaItem
from app.db.memory import db
from app.core.enums import PerfilUsuario


router = APIRouter(
    prefix="/disputa",
    tags=["Disputa"],
)

# =========================
# Schemas (Swagger)
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


# =========================
# Endpoints
# =========================

@router.post("/iniciar", summary="Iniciar disputa da oportunidade")
def api_iniciar_disputa(payload: IniciarDisputaRequest):
    try:
        return iniciar_disputa(payload.oportunidade_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/lance", summary="Registrar lance de um item")
def api_registrar_lance(payload: RegistrarLanceRequest):
    try:
        return registrar_lance(
            disputa_item_id=payload.disputa_item_id,
            preco_unitario=payload.preco_unitario,
            quantidade=payload.quantidade,
            markup_real=payload.markup_real,
            posicao_final=payload.posicao_final,
            lance_vencedor=payload.lance_vencedor,
            perfil_usuario=payload.perfil_usuario,
        )
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/encerrar-item", summary="Encerrar disputa de um item")
def api_encerrar_disputa_item(payload: EncerrarDisputaItemRequest):
    try:
        disputa_item = next(
            (i for i in db["disputa_itens"] if i.id == payload.disputa_item_id),
            None,
        )

        if not disputa_item:
            raise HTTPException(status_code=404, detail="Item de disputa não encontrado.")

        encerrar_disputa_item(
            disputa_item=disputa_item,
            posicao_final=payload.posicao_final,
        )

        return disputa_item

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
