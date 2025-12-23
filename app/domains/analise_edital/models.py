from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid


class AnaliseEditalCreate(BaseModel):
    oportunidade_id: str

    prazo_entrega_dias: int = Field(..., gt=0)
    exige_amostra: bool
    permite_adesao: bool
    exige_garantia_proposta: bool

    local_entrega: str
    observacoes: Optional[str] = ""

    decisao: str = Field(..., pattern="^(SEGUIR|DESISTIR)$")
    motivo_desistencia: Optional[str] = None


class AnaliseEdital(BaseModel):
    id: str
    oportunidade_id: str

    prazo_entrega_dias: int
    exige_amostra: bool
    permite_adesao: bool
    exige_garantia_proposta: bool

    local_entrega: str
    observacoes: Optional[str]

    decisao: str
    motivo_desistencia: Optional[str]

    criado_em: datetime
