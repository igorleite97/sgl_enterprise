from enum import Enum


class StatusDisputa(Enum):
    ABERTA = "aberta"
    ENCERRADA = "encerrada"


class StatusDisputaItem(Enum):
    EM_DISPUTA = "em_disputa"
    ENCERRADO = "encerrado"


class ResultadoDisputaItem(Enum):
    GANHO = "ganho"
    PERDIDO = "perdido"
