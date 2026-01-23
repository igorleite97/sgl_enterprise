# app/domains/captacao/api.py
from fastapi import APIRouter, Depends, HTTPException

from app.domains.captacao.services import (
    registrar_captacao,
    obter_captacao_por_id,
)
from app.domains.captacao.models import CaptacaoInput, ProcessoCaptado
from app.domains.captacao.exceptions import CaptacaoDuplicadaException
from app.core.auth import get_current_user
from app.db.memory import db

router = APIRouter(prefix="/captacao", tags=["Captação"])

@router.get("/{captacao_id}")
def obter_captacao(captacao_id: str):
    try:
        return obter_captacao_por_id(captacao_id)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Captação não encontrada"
        )


@router.get("/", response_model=list[ProcessoCaptado])
def listar_captacoes():
    return db["oportunidades"]



@router.post("/")
def criar_captacao(
    payload: CaptacaoInput,
    usuario: str = Depends(get_current_user),
):
    try:
        return registrar_captacao(payload, usuario)
    except CaptacaoDuplicadaException as e:
        raise HTTPException(
            status_code=409,
            detail={
                "tipo": e.tipo,
                "mensagem": e.mensagem,
                "processoId": e.processo_id,
            },
        )
