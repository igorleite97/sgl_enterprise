def validar_desistencia(data):
    if data["status"] == "desistencia" and not data.get("motivo_desistencia"):
        raise ValueError("Motivo de desistência é obrigatório")


def validar_campos_obrigatorios(data):
    if data["prazo_entrega_dias"] <= 0:
        raise ValueError("Prazo de entrega inválido")
def validar_campos_obrigatorios(data: dict):
    if data["prazo_entrega_dias"] <= 0:
        raise ValueError("Prazo de entrega deve ser maior que zero")


def validar_desistencia(data: dict):
    if data["status"] == "desistencia" and not data.get("motivo_desistencia"):
        raise ValueError("Motivo de desistência é obrigatório")
