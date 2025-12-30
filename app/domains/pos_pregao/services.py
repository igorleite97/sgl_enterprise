from app.db.memory import db, now
from app.domains.pos_pregao.models import PosPregaoItem
from app.domains.pos_pregao.enums import (
    TipoResultadoInicial,
    StatusPosPregao,
)
from app.domains.disputa.enums import ResultadoDisputaItem


def iniciar_pos_pregao(disputa_item) -> PosPregaoItem:
    """
    Cria automaticamente o Pós-Pregão conforme resultado da disputa.
    """

    if disputa_item.posicao_final > 10:
        raise ValueError(
            "Itens acima da 10ª posição não entram em pós-pregão."
        )

    if disputa_item.resultado_final == ResultadoDisputaItem.GANHO:
        tipo = TipoResultadoInicial.GANHO
        status_inicial = StatusPosPregao.ARREMATANTE

    else:
        tipo = TipoResultadoInicial.PERDIDO_MONITORAVEL
        status_inicial = StatusPosPregao.PERDIDO_MONITORAVEL

    pos = PosPregaoItem(
        id=len(db["pos_pregao_itens"]) + 1,
        disputa_item_id=disputa_item.id,
        tipo_resultado_inicial=tipo,
        status_atual=status_inicial,
        iniciado_em=now(),
        atualizado_em=now(),
        encerrado=False,
    )

    db["pos_pregao_itens"].append(pos)
    return pos


def avancar_status(pos: PosPregaoItem, novo_status: StatusPosPregao):
    """
    Avança manualmente o status do pós-pregão.
    """

    if pos.encerrado:
        raise ValueError("Pós-pregão já encerrado.")

    pos.status_atual = novo_status
    pos.atualizado_em = now()


def encerrar_pos_pregao(pos: PosPregaoItem):
    """
    Encerra definitivamente o acompanhamento.
    """

    pos.status_atual = StatusPosPregao.ENCERRADO
    pos.encerrado = True
    pos.atualizado_em = now()
