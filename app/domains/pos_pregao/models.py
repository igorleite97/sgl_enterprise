from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.core.enums import StatusPosPregao
from app.domains.pos_pregao.enums import TipoResultadoInicial



@dataclass
class PosPregaoItem:
    """
    Representa o pós-pregão no nível do ITEM DE DISPUTA.
    Uso interno (engine / regras).
    """

    id: str
    disputa_item_id: str

    tipo_resultado_inicial: TipoResultadoInicial
    status_atual: StatusPosPregao

    iniciado_em: datetime
    atualizado_em: Optional[datetime] = None

    encerrado: bool = False

class PosPregao(BaseModel):
    """
    Representa o Pós-Pregão no nível do PROCESSO.
    Exposto via API.
    """

    id: str
    oportunidade_id: str
    status: StatusPosPregao

    observacao: Optional[str] = None

    criado_em: datetime
    atualizado_em: Optional[datetime] = None

