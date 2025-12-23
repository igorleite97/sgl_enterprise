from enum import Enum


class StatusDisputa(str, Enum):
    ABERTA = "ABERTA"
    ENCERRADA = "ENCERRADA"


class StatusDisputaItem(str, Enum):
    AGUARDANDO_LANCE = "AGUARDANDO_LANCE"
    EM_LANCE = "EM_LANCE"
    FINALIZADO = "FINALIZADO"
