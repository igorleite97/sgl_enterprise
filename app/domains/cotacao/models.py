from pydantic import BaseModel
from typing import Optional
from app.core.enums import StatusCotacaoItem


class CotacaoCreate(BaseModel):
    oportunidade_id: str
    item_id: str
    fabricante: str
    produto: str
    preco_custo: float
    frete: float
    status: StatusCotacaoItem
    justificativa_desistencia: Optional[str] = None


class CotacaoOut(CotacaoCreate):
    id: str
    criado_em: str
