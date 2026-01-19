from datetime import date
from app.domains.alerts.enums import TipoAlerta


def alerta_prazo_entrega(data_entrega: date, hoje: date) -> str | None:
    dias_restantes = (data_entrega - hoje).days

    if dias_restantes < 0:
        return f"Entrega em atraso há {-dias_restantes} dias"

    if dias_restantes <= 3:
        return f"Entrega prevista em {dias_restantes} dias"

    return None


def alerta_saldo_baixo(valor_a_empenhar: float) -> str | None:
    if valor_a_empenhar <= 0:
        return "Contrato sem saldo disponível para empenho"
    return None
