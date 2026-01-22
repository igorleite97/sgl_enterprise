# app/domains/captacao/api.py
from fastapi import APIRouter, Depends, HTTPException

from app.domains.captacao.services import registrar_captacao
from app.domains.captacao.models import CaptacaoInput, ProcessoCaptado
from app.domains.captacao.exceptions import ProcessoDuplicadoError
from app.core.auth import get_current_user

router = APIRouter(prefix="/captacao", tags=["Captação"])

@router.post("", response_model=ProcessoCaptado)
def criar_captacao(
    data: CaptacaoInput,
    user=Depends(get_current_user),
):
    try:
        return registrar_captacao(data=data, usuario=user.nome)
    except ProcessoDuplicadoError as e:
        raise HTTPException(
            status_code=409,
            detail={
                "message": "Processo já cadastrado para este órgão.",
                "processo_id": e.processo_id,
            },
        )

@router.get("/")
def listar_captacoes():
    return db["oportunidades"]
