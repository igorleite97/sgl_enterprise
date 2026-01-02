import uuid
from fastapi import HTTPException

from app.db.memory import db, now
from app.core.enums import StatusProcesso, StatusDisputaItem
from app.domains.timeline.services import registrar_evento
from app.domains.timeline.enums import TipoEventoTimeline, OrigemEvento


# =========================
# PROCESSO → DISPUTA
# =========================

def iniciar_disputa(
    oportunidade_id: str,
    usuario: str = "sistema",
    origem: OrigemEvento = OrigemEvento.SISTEMA,
):
    oportunidade = next(
        (o for o in db["oportunidades"] if o["id"] == oportunidade_id),
        None
    )

    if not oportunidade:
        raise HTTPException(status_code=404, detail="Oportunidade não encontrada")

    if oportunidade["status"] != StatusProcesso.COTACAO_ENCERRADA:
        raise HTTPException(
            status_code=400,
            detail="Disputa só pode ser iniciada após encerramento da cotação."
        )

    for item in oportunidade.get("itens", []):
        disputa_item = {
            "id": str(uuid.uuid4())[:8],
            "oportunidade_id": oportunidade_id,
            "item_id": item["id"],
            "status": StatusDisputaItem.CRIADO,
            "criado_em": now(),
        }
        db["disputa_itens"].append(disputa_item)

    oportunidade["status"] = StatusProcesso.DISPUTA
    oportunidade["atualizada_em"] = now()

    registrar_evento(
        entidade="PROCESSO",
        entidade_id=oportunidade_id,
        tipo_evento=TipoEventoTimeline.STATUS,
        descricao="Disputa iniciada para os itens.",
        origem=origem,
        usuario=usuario,
    )

    return {"status": "DISPUTA_INICIADA"}


# =========================
# ITEM DE DISPUTA
# =========================

def encerrar_disputa_item(
    disputa_item_id: str,
    posicao_final: int,
    usuario: str = "sistema",
    origem: OrigemEvento = OrigemEvento.SISTEMA,
):
    item = next(
        (i for i in db["disputa_itens"] if i["id"] == disputa_item_id),
        None
    )

    if not item:
        raise HTTPException(status_code=404, detail="Item de disputa não encontrado")

    item["status"] = StatusDisputaItem.ENCERRADO
    item["posicao_final"] = posicao_final
    item["atualizada_em"] = now()

    registrar_evento(
        entidade="DISPUTA",
        entidade_id=item["id"],
        tipo_evento=TipoEventoTimeline.DECISAO,
        descricao=f"Item encerrado com posição final {posicao_final}.",
        origem=origem,
        usuario=usuario,
    )

    return item


def registrar_lance(
    disputa_item_id: str,
    preco_unitario: float,
    quantidade: int,
    markup_real: float,
    posicao: int,
    vencedor: bool = False,
    usuario: str = "sistema",
    origem: OrigemEvento = OrigemEvento.SISTEMA,
):
    item = next(
        (i for i in db["disputa_itens"] if i["id"] == disputa_item_id),
        None
    )

    if not item:
        raise HTTPException(status_code=404, detail="Item de disputa não encontrado")

    if item["status"] == StatusDisputaItem.ENCERRADO:
        raise HTTPException(
            status_code=400,
            detail="Não é possível registrar lance em item encerrado"
        )

    lance = {
        "id": str(uuid.uuid4())[:8],
        "disputa_item_id": disputa_item_id,
        "preco_unitario": preco_unitario,
        "quantidade": quantidade,
        "markup_real": markup_real,
        "posicao": posicao,
        "vencedor": vencedor,
        "criado_em": now(),
    }

    db.setdefault("lances", []).append(lance)

    registrar_evento(
        entidade="DISPUTA",
        entidade_id=disputa_item_id,
        tipo_evento=TipoEventoTimeline.OBSERVACAO,
        descricao=(
            f"Lance registrado | "
            f"Preço: {preco_unitario} | "
            f"Qtd: {quantidade} | "
            f"Markup: {markup_real} | "
            f"Posição: {posicao}"
        ),
        origem=origem,
        usuario=usuario,
    )

    item["status"] = StatusDisputaItem.EM_DISPUTA
    item["atualizada_em"] = now()

    return lance

def consolidar_disputa(
    oportunidade_id: str,
    usuario: str = "sistema",
    origem: OrigemEvento = OrigemEvento.SISTEMA,
):
    oportunidade = next(
        (o for o in db["oportunidades"] if o["id"] == oportunidade_id),
        None
    )

    if not oportunidade:
        raise HTTPException(status_code=404, detail="Oportunidade não encontrada")

    itens = [
        i for i in db["disputa_itens"]
        if i["oportunidade_id"] == oportunidade_id
    ]

    if not itens:
        raise HTTPException(
            status_code=400,
            detail="Nenhum item de disputa encontrado para consolidação"
        )

    pendentes = [
        i for i in itens
        if i["status"] != StatusDisputaItem.ENCERRADO
    ]

    if pendentes:
        raise HTTPException(
            status_code=400,
            detail="Ainda existem itens de disputa não encerrados"
        )

    oportunidade["status"] = StatusProcesso.POS_PREGAO
    oportunidade["atualizada_em"] = now()

    registrar_evento(
        entidade="PROCESSO",
        entidade_id=oportunidade_id,
        tipo_evento=TipoEventoTimeline.STATUS,
        descricao="Todos os itens encerrados. Processo avançou para Pós-Pregão.",
        origem=origem,
        usuario=usuario,
    )

    return {"status": "POS_PREGAO"}
