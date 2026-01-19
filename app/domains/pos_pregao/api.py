from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.domains.pos_pregao.services import (
    iniciar_pos_pregao,
    confirmar_homologacao,
)

router = APIRouter(
    prefix="/pos-pregao",
    tags=["Pós-Pregão"],
)


class IniciarPosPregaoRequest(BaseModel):
    oportunidade_id: str


class ConfirmarHomologacaoRequest(BaseModel):
    oportunidade_id: str


@router.post("/iniciar", summary="Iniciar pós-pregão da oportunidade")
def api_iniciar_pos_pregao(payload: IniciarPosPregaoRequest):
    try:
        return iniciar_pos_pregao(payload.oportunidade_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/confirmar-homologacao",
    summary="Confirmar homologação e gerar contrato em STANDBY"
)
def api_confirmar_homologacao(payload: ConfirmarHomologacaoRequest):
    try:
        return confirmar_homologacao(payload.oportunidade_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
