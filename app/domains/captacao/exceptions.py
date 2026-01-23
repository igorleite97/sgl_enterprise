class CaptacaoDuplicadaException(Exception):
    def __init__(self, processo_id: str):
        self.tipo = "CAPTACAO_DUPLICADA"
        self.mensagem = "Já existe um processo cadastrado com esta UASG e número."
        self.processo_id = processo_id
