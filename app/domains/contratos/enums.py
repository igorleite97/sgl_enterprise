from enum import Enum

class StatusContrato(str, Enum):
    CRIADO = "CRIADO"
    RECEBIDO = "RECEBIDO"
    ATIVO = "ATIVO"         # Contrato recebido e vigente
    SUSPENSO = "SUSPENSO"
    ENCERRADO = "ENCERRADO"
    CANCELADO = "CANCELADO"
    
