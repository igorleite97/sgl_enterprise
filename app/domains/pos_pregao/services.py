import uuid
from app.db.memory import db, now
from app.domains.pos_pregao.enums import StatusPosPregao
from app.domains.contratos.services import criar_contrato_standby


def iniciar_pos_pregao(oportunidade_id: str):
    oportunidade = next(
        (o for o in db["oportunidades"] if o["id"] == oportunidade_id),
        None
    )

    if not oportunidade:
        raise ValueError("Oportunidade não encontrada.")

    # Valida se houve disputa encerrada
    itens_disputa = [
        i for i in db["disputa_itens"]
        if i["oportunidade_id"] == oportunidade_id
    ]

    if not itens_disputa:
        raise ValueError("Não existem itens de disputa para esta oportunidade.")

    # Evita duplicidade
    existente = next(
        (p for p in db["pos_pregao"] if p["oportunidade_id"] == oportunidade_id),
        None
    )

    if existente:
        return existente

    pos_pregao = {
        "id": str(uuid.uuid4())[:8],
        "oportunidade_id": oportunidade_id,

        # Status correto para início do pós-pregão
        "status": StatusPosPregao.ARREMATANTE,

        "criado_em": now(),
        "atualizado_em": now(),
    }

    db["pos_pregao"].append(pos_pregao)
    return pos_pregao

def confirmar_homologacao(
    oportunidade_id: str,
    usuario: str = "sistema"
):
    # Localiza o pós-pregão
    pos_pregao = next(
        (p for p in db["pos_pregao"] if p["oportunidade_id"] == oportunidade_id),
        None
    )

    if not pos_pregao:
        raise ValueError("Pós-pregão não encontrado.")

    # Validação de estado
    if pos_pregao["status"] != StatusPosPregao.ARREMATANTE:
        raise ValueError(
            f"Homologação só pode ocorrer se status for ARREMATANTE. "
            f"Status atual: {pos_pregao['status']}"
        )

    # Atualiza status do pós-pregão
    pos_pregao["status"] = StatusPosPregao.HABILITADO
    pos_pregao["atualizado_em"] = now()

    # 🔥 GATILHO AUTOMÁTICO → CONTRATO STANDBY
    contrato = criar_contrato_standby(
        oportunidade_id=oportunidade_id,
        pos_pregao_id=pos_pregao["id"],
        usuario=usuario,
    )

    return {
        "pos_pregao": pos_pregao,
        "contrato": contrato,
    }