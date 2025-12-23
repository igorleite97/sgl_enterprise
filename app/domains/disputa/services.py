from app.db.memory import db, now
from app.core.enums import StatusProcesso, StatusCotacaoItem
from app.domains.disputa.enums import StatusDisputa, StatusDisputaItem
from app.domains.disputa.models import Disputa, DisputaItem

MARKUP_MINIMO_PADRAO = 1.30


def iniciar_disputa(oportunidade_id: int) -> Disputa:
    """
    Inicia a disputa e cria automaticamente os DisputaItem
    apenas para itens com status COTADO.
    """

    # Validação crítica
    cotacoes_cotadas = [
        c for c in db["cotacoes"].values()
        if c["oportunidade_id"] == oportunidade_id
        and c["status"] == StatusCotacaoItem.COTADO
    ]

    if not cotacoes_cotadas:
        raise ValueError(
            "Não é possível iniciar a disputa: nenhum item foi cotado."
        )

    # Atualiza status do processo
    for oportunidade in db["oportunidades"].values():
        if oportunidade["id"] == oportunidade_id:
            oportunidade["status"] = StatusProcesso.DISPUTA
            oportunidade["atualizado_em"] = now()
            break
    else:
        raise ValueError("Oportunidade não encontrada.")

    # Cria Disputa
    disputa_id = len(db["disputas"]) + 1

    disputa = Disputa(
        id=disputa_id,
        oportunidade_id=oportunidade_id,
        status=StatusDisputa.ABERTA,
        criada_em=now(),
    )

    db["disputas"][disputa_id] = disputa

    # Cria DisputaItem para cada cotação
    for cotacao in cotacoes_cotadas:
        disputa_item_id = len(db["disputa_itens"]) + 1

        preco_base = cotacao["preco_unitario"]
        preco_minimo = preco_base * MARKUP_MINIMO_PADRAO

        disputa_item = DisputaItem(
            id=disputa_item_id,
            disputa_id=disputa_id,
            item_id=cotacao["item_id"],
            preco_base=preco_base,
            markup_aplicado=MARKUP_MINIMO_PADRAO,
            preco_minimo_permitido=preco_minimo,
            preco_atual=preco_minimo,
            autorizacao_excecao=False,
            status=StatusDisputaItem.AGUARDANDO_LANCE,
        )

        db["disputa_itens"][disputa_item_id] = disputa_item

    return disputa
