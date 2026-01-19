from app.domains.contratos.enums import StatusContrato

TRANSICOES_CONTRATO = {
    StatusContrato.CRIADO: {
        StatusContrato.RECEBIDO,
        StatusContrato.CANCELADO,
    },
    StatusContrato.RECEBIDO: {
        StatusContrato.ATIVO,
        StatusContrato.CANCELADO,
    },
    StatusContrato.ATIVO: {
        StatusContrato.SUSPENSO,
        StatusContrato.ENCERRADO,
    },
    StatusContrato.SUSPENSO: {
        StatusContrato.ATIVO,
        StatusContrato.CANCELADO,
    },
    StatusContrato.ENCERRADO: set(),
    StatusContrato.CANCELADO: set(),
}

def validar_transicao_contrato(
    status_atual: StatusContrato,
    novo_status: StatusContrato,
):
    permitidos = TRANSICOES_CONTRATO.get(status_atual, set())

    if novo_status not in permitidos:
        raise ValueError(
            f"Transição inválida: {status_atual.value} → {novo_status.value}"
        )
