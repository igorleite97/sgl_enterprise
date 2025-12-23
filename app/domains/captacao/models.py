# app/domains/captacao/models.py

from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
import uuid

from app.core.enums import StatusProcesso


class ItemCaptado(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    numero_item: str
    subgrupo: str
    valor_referencia: float
    quantidade: float


class CaptacaoInput(BaseModel):
    numero_processo: str
    uasg: str
    orgao: str
    portal: str
    data_hora_disputa: datetime
    itens: List[ItemCaptado]


class ProcessoCaptado(BaseModel):
    id: str
    numero_processo: str
    uasg: str
    orgao: str
    portal: str
    data_hora_disputa: datetime
    status: StatusProcesso
    itens: List[ItemCaptado]
    criado_em: str
