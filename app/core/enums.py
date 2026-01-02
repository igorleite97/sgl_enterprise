from enum import Enum


# =========================
# MACROFLUXO DO PROCESSO
# =========================
class StatusProcesso(str, Enum):
    CAPTACAO = "CAPTACAO"
    ANALISE_EDITAL = "ANALISE_EDITAL"
    ANALISE_APROVADA = "ANALISE_APROVADA"
    DESISTENCIA = "DESISTENCIA"
    COTACAO = "COTACAO"
    COTACAO_INICIADA = "COTACAO_INICIADA"
    COTACAO_ENCERRADA = "COTACAO_ENCERRADA"
    DISPUTA = "DISPUTA"
    POS_PREGAO = "POS_PREGAO"
    CONTRATO = "CONTRATO"


# =========================
# MICROFLUXO DA DISPUTA (ITEM)
# =========================
class StatusDisputaItem(str, Enum):
    CRIADO = "CRIADO"
    EM_DISPUTA = "EM_DISPUTA"
    VENCEDOR = "VENCEDOR"
    PERDEDOR = "PERDEDOR"
    DESCLASSIFICADO = "DESCLASSIFICADO"
    ENCERRADO = "ENCERRADO"


# =========================
# PERFIL DE USUÁRIO
# =========================
class PerfilUsuario(str, Enum):
    ANALISTA = "ANALISTA"
    GESTOR = "GESTOR"


# =========================
# TIMELINE / AUDITORIA
# =========================
class DominioEvento(str, Enum):
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


# =========================
# TIMELINE / AUDITORIA PÓS-PREGÃO
# =========================

class StatusPosPregao(str, Enum):
    EM_ANALISE = "EM_ANALISE"
    HABILITADO = "HABILITADO"
    INABILITADO = "INABILITADO"
    EM_RECURSO = "EM_RECURSO"
    HOMOLOGADO = "HOMOLOGADO"