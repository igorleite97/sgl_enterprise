from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from app.core.enums import StatusProcesso


# ==============================
# INPUT
# ==============================
class CotacaoCreate(BaseModel):
    oportunidade_id: str
    fornecedor: str
    valor_total: float
    prazo_entrega_dias: int
    observacoes: Optional[str] = None


# ==============================
# DOMÍNIO (uso interno / services)
# ==============================
class Cotacao(BaseModel):
    id: str
    oportunidade_id: str
    fornecedor: str
    valor_total: float
    prazo_entrega_dias: int
    observacoes: Optional[str] = None
    status: StatusProcesso
    criado_em: datetime
    atualizada_em: Optional[datetime] = None


# ==============================
# OUTPUT (API)
# ==============================
class CotacaoRead(Cotacao):
    pass
