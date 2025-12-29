from dataclasses import dataclass
from datetime import datetime
from app.domains.disputa.enums import (
    StatusDisputa,
    StatusDisputaItem,
    ResultadoDisputaItem,
)


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
    resultado_final: ResultadoDisputaItem | None
    em_monitoramento_pos: bool


@dataclass
class Lance:
    id: int
    disputa_item_id: int

    preco_unitario_lance: float
    quantidade: int
    preco_total_lance: float

    markup_aplicado_real: float

    posicao_final: int
    lance_vencedor: float | None

    abaixo_markup_minimo: bool
    autorizacao_excecao: bool

    criado_em: datetime
