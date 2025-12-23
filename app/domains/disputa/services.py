from app.db.memory import db, now
from app.core.enums import StatusProcesso, StatusCotacaoItem


def _existe_item_cotado(oportunidade_id: str) -> bool:
    """
    Regra crítica:
    Só permite avançar para disputa se existir ao menos
    um item com status COTADO.
    """
    for cotacao in db["cotacoes"]:
        if (
            cotacao["oportunidade_id"] == oportunidade_id
            and cotacao["status"] == StatusCotacaoItem.COTADO
        ):
            return True
    return False


def iniciar_disputa(oportunidade_id: str):
    # Regra obrigatória
    if not _existe_item_cotado(oportunidade_id):
        raise ValueError(
            "Não é possível iniciar a disputa: nenhum item foi cotado."
        )

    # Atualiza status do processo
    for processo in db["oportunidades"]:
        if processo["id"] == oportunidade_id:
            processo["status"] = StatusProcesso.DISPUTA
            processo["atualizado_em"] = now()
            return processo

    raise ValueError("Oportunidade não encontrada.")