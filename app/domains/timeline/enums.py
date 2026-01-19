from enum import Enum


class TipoEventoTimeline(str, Enum):
    CRIACAO = "criacao"
    STATUS = "status"
    OBSERVACAO = "observacao"
    DECISAO = "decisao"


class SeveridadeEvento(str, Enum):
    BAIXA = "baixa"
    MEDIA = "media"
    ALTA = "alta"
    CRITICA = "critica"
