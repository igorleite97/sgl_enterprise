from dataclasses import dataclass
from datetime import datetime
from app.domains.pos_pregao.enums import (
    TipoResultadoInicial,
    StatusPosPregao,
)


@dataclass
class PosPregaoItem:
    id: int
    disputa_item_id: int

    tipo_resultado_inicial: TipoResultadoInicial
    status_atual: StatusPosPregao

    iniciado_em: datetime
    atualizado_em: datetime

    encerrado: bool
