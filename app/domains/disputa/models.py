from dataclasses import dataclass
from datetime import datetime
from app.domains.disputa.enums import StatusDisputa, StatusDisputaItem


@dataclass
class Disputa:
    id: int
    oportunidade_id: int
    status: StatusDisputa
    criada_em: datetime


@dataclass
class DisputaItem:
    id: int
    disputa_id: int
    item_id: int
    preco_base: float
    markup_aplicado: float
    preco_minimo_permitido: float
    preco_atual: float
    autorizacao_excecao: bool
    status: StatusDisputaItem
