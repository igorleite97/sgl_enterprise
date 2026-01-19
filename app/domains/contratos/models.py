from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from app.domains.contratos.enums import StatusContrato

@dataclass
class Contrato:
    id: str
    oportunidade_id: str
    pos_pregao_id: str

    status: StatusContrato  # STANDBY | ATIVO | VENCIDO | ENCERRADO

    numero_contrato: Optional[str] = None
    data_inicio: Optional[datetime] = None
    data_fim: Optional[datetime] = None

    criado_em: datetime
    atualizado_em: Optional[datetime] = None


@dataclass
class ContratoItem:
    id: str
    contrato_id: str
    disputa_item_id: str

    quantidade_total: int
    quantidade_empenhada: int = 0

    valor_unitario: float = 0.0

    @property
    def quantidade_a_empenhar(self):
        return self.quantidade_total - self.quantidade_empenhada

@dataclass
class EmpenhoItem:
    id: str
    empenho_id: str  # id interno do sistema
    numero_empenho: str  # ex: 2026NE387 (único, oficial)

    contrato_item_id: str

    quantidade_empenhada: int
    valor_unitario: float
    valor_total: float

    criado_em: datetime

