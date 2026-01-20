from app.db.memory import db
from app.domains.alerts.services import (
    gerar_alertas_empenhos,
    gerar_alertas_contratos,
)
from app.domains.alerts.enums import TipoAlerta


def alerta_ja_existe(tipo: TipoAlerta, entidade: str, entidade_id: str) -> bool:
    """
    Evita geração duplicada de alertas ativos
    """
    for alerta in db.get("alertas", []):
        if (
            alerta.tipo == tipo
            and alerta.entidade == entidade
            and alerta.entidade_id == entidade_id
            and alerta.status == "ATIVO"
        ):
            return True
    return False


def executar_orquestrador_alertas(usuario: str = "sistema"):
    """
    Ponto único de execução de alertas do sistema.
    Pode ser chamado por:
    - scheduler
    - endpoint interno
    - eventos futuros
    """

    # ALERTAS DE EMPENHOS
    gerar_alertas_empenhos(usuario=usuario)

    # ALERTAS DE CONTRATOS
    gerar_alertas_contratos(usuario=usuario)
