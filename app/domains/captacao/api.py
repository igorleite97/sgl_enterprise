# app/domains/captacao/api.py

from fastapi import APIRouter
from app.domains.captacao.models import CaptacaoInput, ProcessoCaptado
from app.domains.captacao.services import registrar_captacao
from app.db.memory import db

router = APIRouter(prefix="/captacao", tags=["Captação"])


@router.post("/", response_model=ProcessoCaptado)
def criar_captacao(data: CaptacaoInput):
    return registrar_captacao(data)


@router.get("/")
def listar_captacoes():
    return db["oportunidades"]
