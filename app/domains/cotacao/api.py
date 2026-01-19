from fastapi import APIRouter

from app.domains.cotacao.models import CotacaoCreate, CotacaoRead
from app.domains.cotacao.services import (
    criar_cotacao,
    obter_cotacao,
    listar_por_oportunidade,
)

router = APIRouter(
    prefix="/cotacoes",
    tags=["Cotação"],
)


@router.post("/", response_model=CotacaoRead)
def criar(
    data: CotacaoCreate,
    usuario: str = "api_user",
):
    return criar_cotacao(
        data=data,
        usuario=usuario,
    )


@router.get("/{cotacao_id}", response_model=CotacaoRead)
def obter(cotacao_id: str):
    return obter_cotacao(cotacao_id)


@router.get("/oportunidade/{oportunidade_id}", response_model=list[CotacaoRead])
def listar(oportunidade_id: str):
    return listar_por_oportunidade(oportunidade_id)
