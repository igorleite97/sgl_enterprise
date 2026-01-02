import uuid
from app.db.memory import db, now


def iniciar_pos_pregao(oportunidade_id: str):
    oportunidade = next(
        (o for o in db["oportunidades"] if o["id"] == oportunidade_id),
        None
    )

    if not oportunidade:
        raise ValueError("Oportunidade não encontrada.")

    pos_pregao = {
        "id": str(uuid.uuid4())[:8],
        "oportunidade_id": oportunidade_id,
        "status": "EM_CONFERENCIA",
        "criado_em": now(),
        "atualizado_em": now(),
    }

    db["pos_pregao"].append(pos_pregao)

    # Consolidação item a item
    for item in db["disputa_itens"]:
        if item["oportunidade_id"] != oportunidade_id:
            continue

        lance_vencedor = next(
            (
                l for l in db["lances"]
                if l["disputa_item_id"] == item["id"]
                and l.get("vencedor") is True
            ),
            None
        )

        if not lance_vencedor:
            continue

        pos_item = {
            "id": str(uuid.uuid4())[:8],
            "pos_pregao_id": pos_pregao["id"],
            "disputa_item_id": item["id"],

            "tipo_resultado_inicial": "VENCEDOR",
            "status_atual": "ARREMATANTE",
            "encerrado": False,

            "quantidade_arrematada": lance_vencedor["quantidade"],
            "valor_unitario_arrematado": lance_vencedor["preco_unitario"],
            "valor_total_arrematado": (
                lance_vencedor["quantidade"] * lance_vencedor["preco_unitario"]
    ),

        "criado_em": now(),
        "atualizado_em": now(),
}


        db["pos_pregao_itens"].append(pos_item)

    return pos_pregao
