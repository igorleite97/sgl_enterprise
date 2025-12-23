from fastapi import APIRouter, HTTPException
from typing import List
from app.domains.cotacao.models import CotacaoCreate, CotacaoOut
from app.domains.cotacao.services import (
    criar_cotacao,
    listar_por_oportunidade,
    listar_por_item,
)

router = APIRouter(prefix="/cotacao", tags=["Cotação"])


@router.post("/", response_model=CotacaoOut)
def criar(data: CotacaoCreate):
    try:
        return criar_cotacao(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/por-oportunidade/{oportunidade_id}", response_model=List[CotacaoOut])
def listar_oportunidade(oportunidade_id: str):
    return listar_por_oportunidade(oportunidade_id)


@router.get("/por-item/{item_id}", response_model=List[CotacaoOut])
def listar_item(item_id: str):
    return listar_por_item(item_id)
