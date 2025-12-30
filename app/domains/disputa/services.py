from app.db.memory import db, now
from app.domains.disputa.enums import (
    StatusDisputa,
    StatusDisputaItem,
    ResultadoDisputaItem,
)
from app.domains.disputa.models import Disputa, DisputaItem, Lance
from app.domains.disputa.constants import MARKUP_MINIMO_AUTORIZADO
from app.core.enums import PerfilUsuario
from app.domains.pos_pregao.services import iniciar_pos_pregao


def iniciar_disputa(oportunidade_id: int) -> Disputa:
    disputa = Disputa(
        id=len(db["disputas"]) + 1,
        oportunidade_id=oportunidade_id,
        status=StatusDisputa.ABERTA,
        criada_em=now(),
    )
    db["disputas"].append(disputa)
    return disputa


def registrar_lance(
    disputa_item_id: int,
    preco_unitario: float,
    quantidade: int,
    markup_real: float,
    posicao_final: int,
    lance_vencedor: float | None,
    perfil_usuario: PerfilUsuario,
) -> Lance:
    """
    Regras:
    - Markup mínimo padrão: 1.30
    - Apenas GESTOR pode autorizar exceção
    """

    if markup_real < MARKUP_MINIMO_AUTORIZADO:
        if perfil_usuario != PerfilUsuario.GESTOR:
            raise PermissionError(
                "Apenas gestores podem registrar lance abaixo do markup mínimo."
            )
        autorizacao_excecao = True
    else:
        autorizacao_excecao = False

    preco_total = preco_unitario * quantidade

    lance = Lance(
        id=len(db["lances"]) + 1,
        disputa_item_id=disputa_item_id,
        preco_unitario_lance=preco_unitario,
        quantidade=quantidade,
        preco_total_lance=preco_total,
        markup_aplicado_real=markup_real,
        posicao_final=posicao_final,
        lance_vencedor=lance_vencedor,
        abaixo_markup_minimo=markup_real < MARKUP_MINIMO_AUTORIZADO,
        autorizacao_excecao=autorizacao_excecao,
        criado_em=now(),
    )

    db["lances"].append(lance)
    return lance


def encerrar_disputa_item(
    disputa_item: DisputaItem,
    posicao_final: int,
):
    """
    Encerra o item de disputa e,
    se aplicável, cria automaticamente o Pós-Pregão.
    """

    # Define resultado
    if posicao_final == 1:
        disputa_item.resultado_final = ResultadoDisputaItem.GANHO
        disputa_item.em_monitoramento_pos = False

    elif 2 <= posicao_final <= 10:
        disputa_item.resultado_final = ResultadoDisputaItem.PERDIDO
        disputa_item.em_monitoramento_pos = True

    else:
        disputa_item.resultado_final = ResultadoDisputaItem.PERDIDO
        disputa_item.em_monitoramento_pos = False

    disputa_item.status = StatusDisputaItem.ENCERRADO

    # 🔗 Amarra automaticamente com Pós-Pregão
    if posicao_final <= 10:
        iniciar_pos_pregao(disputa_item)
