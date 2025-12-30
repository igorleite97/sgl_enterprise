from enum import Enum


class TipoEventoTimeline(str, Enum):
    CRIACAO = "CRIACAO"
    ATUALIZACAO = "ATUALIZACAO"
    DECISAO = "DECISAO"
    STATUS = "STATUS"
    AUDITORIA = "AUDITORIA"


class OrigemEvento(str, Enum):
    SISTEMA = "SISTEMA"
    USUARIO = "USUARIO"
