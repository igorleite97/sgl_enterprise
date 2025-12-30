from enum import Enum

class StatusProcesso(str, Enum):
    CAPTACAO = "CAPTACAO"
    ANALISE_EDITAL = "ANALISE_EDITAL"
    COTACAO = "COTACAO"
    DISPUTA = "DISPUTA"
    POS_PREGAO = "POS_PREGAO"
    CONTRATO = "CONTRATO"
    DESISTIDO = "DESISTIDO"


class StatusAnaliseEdital(str, Enum):
    PENDENTE = "PENDENTE"
    APROVADA = "APROVADA"
    DESISTIDO = "DESISTIDO"

from enum import Enum


class StatusCotacaoItem(str, Enum):
    COTADO = "COTADO"
    DESISTIDO = "DESISTIDO"

from enum import Enum


class PerfilUsuario(str, Enum):
    ANALISTA = "ANALISTA"
    GESTOR = "GESTOR"

from enum import Enum

class DominioEvento (str, Enum):
    PROCESSO = "PROCESSO"
    CAPTACAO = "CAPTACAO"
    ANALISE_EDITAL = "ANALISE_EDITAL"
    COTACAO = "COTACAO"
    DISPUTA = "DISPUTA"
    POS_PREGAO = "POS_PREGAO"
    CONTRATO = "CONTRATO"

class TipoEvento(str, Enum):
    CRIACAO = "CRIACAO"
    ATUALIZACAO_STATUS = "ATUALIZACAO_STATUS"
    DECISAO = "DECISAO"
    EXCECAO = "EXCECAO"
    OBSERVACAO = "OBSERVACAO"
