from fastapi import APIRouter
from app.domains.analise_edital.models import AnaliseEditalCreate, AnaliseEdital
from app.domains.analise_edital.services import (
    criar_analise_edital,
    obter_analise,
    listar_por_oportunidade
)

router = APIRouter(prefix="/analise-edital", tags=["Análise de Edital"])


@router.post("/", response_model=AnaliseEdital)
def criar(data: AnaliseEditalCreate):
    return criar_analise_edital(data)


@router.get("/{analise_id}")
def obter(analise_id: str):
    return obter_analise(analise_id)


@router.get("/por-oportunidade/{oportunidade_id}")
def listar(oportunidade_id: str):
    return listar_por_oportunidade(oportunidade_id)
