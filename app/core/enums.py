from enum import Enum

class StatusProcesso(str, Enum):
    CAPTACAO = "CAPTACAO"
    ANALISE_EDITAL = "ANALISE_EDITAL"
    DESISTENCIA = "DESISTENCIA"

from enum import Enum


class StatusProcesso(str, Enum):
    CAPTACAO = "CAPTACAO"
    ANALISE_EDITAL = "ANALISE_EDITAL"
    COTACAO = "COTACAO"
    DISPUTA = "DISPUTA"
    POS_PREGAO = "POS_PREGAO"
    CONTRATO = "CONTRATO"


class StatusAnaliseEdital(str, Enum):
    PENDENTE = "PENDENTE"
    APROVADA = "APROVADA"
    DESISTIDO = "DESISTIDO"

from enum import Enum


class StatusCotacaoItem(str, Enum):
    COTADO = "COTADO"
    DESISTIDO = "DESISTIDO"
