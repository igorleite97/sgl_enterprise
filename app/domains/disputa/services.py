from app.db.memory import db, now
from app.domains.disputa.enums import (
    StatusDisputa,
    StatusDisputaItem,
    ResultadoDisputaItem,
)
from app.domains.disputa.models import Disputa, DisputaItem, Lance
from app.domains.disputa.constants import MARKUP_MINIMO_AUTORIZADO
from app.core.enums import PerfilUsuario
from app.domains.timeline.services import registrar_evento
from app.domains.timeline.enums import TipoEventoTimeline, OrigemEvento


# =========================================================
# HELPERS DE STATUS (ÚNICA FONTE DE VERDADE)
# =========================================================

def alterar_status_disputa(
    disputa: Disputa,
    novo_status: StatusDisputa,
    usuario: str,
    origem: OrigemEvento,
    justificativa: str | None = None,
) -> None:
    status_anterior = disputa.status

    if status_anterior == novo_status:
        raise ValueError("A disputa já está neste status.")

    disputa.status = novo_status
    disputa.atualizada_em = now()

    descricao = (
        f"Status da disputa alterado de {status_anterior.value} "
        f"para {novo_status.value}."
    )

    if justificativa:
        descricao += f" Justificativa: {justificativa}"

    registrar_evento(
        entidade="DISPUTA",
        entidade_id=disputa.id,
        tipo_evento=TipoEventoTimeline.STATUS,
        descricao=descricao,
        origem=origem,
        usuario=usuario,
    )


def alterar_status_disputa_item(
    disputa_item: DisputaItem,
    novo_status: StatusDisputaItem,
    usuario: str,
    origem: OrigemEvento,
    justificativa: str | None = None,
) -> None:
    status_anterior = disputa_item.status

    if status_anterior == novo_status:
        raise ValueError("O item de disputa já está neste status.")

    disputa_item.status = novo_status
    disputa_item.atualizada_em = now()

    descricao = (
        f"Status do item alterado de {status_anterior.value} "
        f"para {novo_status.value}."
    )

    if justificativa:
        descricao += f" Justificativa: {justificativa}"

    registrar_evento(
        entidade="DISPUTA_ITEM",
        entidade_id=disputa_item.id,
        tipo_evento=TipoEventoTimeline.STATUS,
        descricao=descricao,
        origem=origem,
        usuario=usuario,
    )


# =========================================================
# DISPUTA
# =========================================================

def iniciar_disputa(oportunidade_id: int) -> Disputa:
    disputa = Disputa(
        id=len(db["disputas"]) + 1,
        oportunidade_id=oportunidade_id,
        status=StatusDisputa.CRIADA,
        criada_em=now(),
    )

    db["disputas"].append(disputa)

    alterar_status_disputa(
        disputa=disputa,
        novo_status=StatusDisputa.ABERTA,
        usuario="system",
        origem=OrigemEvento.SISTEMA,
        justificativa="Disputa iniciada automaticamente após conclusão da cotação.",
    )

    return disputa


def encerrar_disputa(
    disputa: Disputa,
    usuario: str,
    origem: OrigemEvento,
    justificativa: str | None = None,
) -> None:
    if disputa.status != StatusDisputa.ABERTA:
        raise ValueError("A disputa só pode ser encerrada se estiver ABERTA.")

    itens_disputa = [
        item for item in db["disputa_itens"]
        if item.disputa_id == disputa.id
    ]

    if not itens_disputa:
        raise ValueError("Não existem itens associados a esta disputa.")

    itens_abertos = [
        item for item in itens_disputa
        if item.status != StatusDisputaItem.ENCERRADO
    ]

    if itens_abertos:
        raise ValueError(
            "Não é possível encerrar a disputa enquanto houver itens em aberto."
        )

    alterar_status_disputa(
        disputa=disputa,
        novo_status=StatusDisputa.ENCERRADA,
        usuario=usuario,
        origem=origem,
        justificativa=justificativa or "Encerramento formal da disputa.",
    )


# =========================================================
# LANCES
# =========================================================

def registrar_lance(
    disputa_item_id: int,
    preco_unitario: float,
    quantidade: int,
    markup_real: float,
    posicao_final: int,
    lance_vencedor: float | None,
    perfil_usuario: PerfilUsuario,
) -> Lance:
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

    registrar_evento(
        entidade="LANCE",
        entidade_id=lance.id,
        tipo_evento=TipoEventoTimeline.DECISAO,
        descricao=(
            f"Lance registrado com markup {markup_real}. "
            f"Posição final: {posicao_final}. "
            f"{'Com exceção autorizada.' if autorizacao_excecao else 'Sem exceção.'}"
        ),
        origem=OrigemEvento.USUARIO,
        usuario=perfil_usuario.value,
    )

    return lance


# =========================================================
# DISPUTA ITEM
# =========================================================

def encerrar_disputa_item(
    disputa_item: DisputaItem,
    posicao_final: int,
) -> None:
    if posicao_final == 1:
        disputa_item.resultado_final = ResultadoDisputaItem.GANHO
        disputa_item.em_monitoramento_pos = False
    elif 2 <= posicao_final <= 10:
        disputa_item.resultado_final = ResultadoDisputaItem.PERDIDO
        disputa_item.em_monitoramento_pos = True
    else:
        disputa_item.resultado_final = ResultadoDisputaItem.PERDIDO
        disputa_item.em_monitoramento_pos = False

    alterar_status_disputa_item(
        disputa_item=disputa_item,
        novo_status=StatusDisputaItem.ENCERRADO,
        usuario="system",
        origem=OrigemEvento.SISTEMA,
        justificativa=f"Encerramento automático após posição final {posicao_final}",
    )

    registrar_evento(
        entidade="DISPUTA_ITEM",
        entidade_id=disputa_item.id,
        tipo_evento=TipoEventoTimeline.ENCERRAMENTO,
        descricao=f"Item encerrado na posição {posicao_final}.",
        origem=OrigemEvento.SISTEMA,
        usuario="system",
    )

    if posicao_final <= 10:
        from app.domains.pos_pregao.services import iniciar_pos_pregao
        iniciar_pos_pregao(disputa_item)
