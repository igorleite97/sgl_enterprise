import re

def normalizar_numero_processo(numero: str) -> str:
    """
    Normaliza o número do processo para evitar duplicidade lógica.
    Exemplos aceitos:
    - 90012/2026
    - 90012-2026
    - 90012 2026
    - 532025
    - 53/2025
    """
    numero = numero.strip().upper()
    numero = re.sub(r"[\/\\_\s]+", "-", numero)
    return numero
