class ProcessoDuplicadoError(Exception):
    def __init__(self, processo_id: str):
        self.processo_id = processo_id
        super().__init__("Processo já captado anteriormente.")
