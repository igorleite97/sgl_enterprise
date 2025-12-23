from pydantic import BaseModel
from typing import Optional


class AnaliseEditalCreate(BaseModel):
    oportunidade_id: str

    prazo_entrega_dias: int
    exigencia_amostra: bool
    adesao: bool

    garantia_contratual_valor: Optional[float] = None
    garantia_contratual_tipo: Optional[str] = None
    garantia_proposta: Optional[bool] = None

    multas: Optional[str] = None
    exigencias_tecnicas: Optional[str] = None
    documentacao: Optional[str] = None
    criterios_julgamento: Optional[str] = None

    status: str
    motivo_desistencia: Optional[str] = None
    observacoes: Optional[str] = None
from typing import Optional
from pydantic import BaseModel


class AnaliseEditalCreate(BaseModel):
    oportunidade_id: str

    prazo_entrega_dias: int
    exigencia_amostra: bool
    adesao: bool

    garantia_contratual_valor: Optional[float] = None
    garantia_contratual_tipo: Optional[str] = None
    garantia_proposta: Optional[bool] = None

    multas: Optional[str] = None
    exigencias_tecnicas: Optional[str] = None
    documentacao: Optional[str] = None
    criterios_julgamento: Optional[str] = None

    status: str
    motivo_desistencia: Optional[str] = None
    observacoes: Optional[str] = None
