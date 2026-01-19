import uuid
from app.db.memory import db, now
from app.domains.contratos.enums import StatusContrato
from app.domains.contratos.rules import validar_transicao_contrato
from app.domains.timeline.services import registrar_evento_timeline
from app.domains.timeline.enums import TipoEventoTimeline

def criar_contrato_standby(
    oportunidade_id: str,
    pos_pregao_id: str,
    usuario: str,
):
    contrato = {
        "id": str(uuid.uuid4())[:8],
        "oportunidade_id": oportunidade_id,
        "pos_pregao_id": pos_pregao_id,
        "status": StatusContrato.STANDBY,
        "numero_contrato": None,
        "data_inicio": None,
        "data_fim": None,
        "criado_em": now(),
        "atualizado_em": None,
    }

    db["contratos"].append(contrato)

    # Itens ainda NÃO nascem aqui (saldo bloqueado)
    return contrato
    

def receber_contrato_ou_ata(
    contrato_id: str,
    numero_documento: str,
    data_inicio,
    data_fim,
    usuario: str = "sistema",
):
    contrato = next(
        (c for c in db["contratos"] if c["id"] == contrato_id),
        None
    )

    if not contrato:
        raise ValueError("Contrato não encontrado.")

    if contrato["status"] != StatusContrato.STANDBY:
        raise ValueError(
            f"Contrato só pode ser ativado se estiver em STANDBY. "
            f"Status atual: {contrato['status']}"
        )

    # 🔹 Busca itens do pós-pregão
    pos_itens = [
        i for i in db["pos_pregao_itens"]
        if i["pos_pregao_id"] == contrato["pos_pregao_id"]
    ]

    if not pos_itens:
        raise ValueError("Nenhum item encontrado no pós-pregão.")

    valor_total = 0.0
    contrato_itens = []

    for item in pos_itens:
        total_item = item["valor_total_arrematado"]
        valor_total += total_item

        contrato_itens.append({
            "id": f"ci-{item['id']}",
            "contrato_id": contrato_id,
            "disputa_item_id": item["disputa_item_id"],

            "quantidade_total": item["quantidade_arrematada"],
            "quantidade_empenhada": 0,

            "valor_unitario": item["valor_unitario_arrematado"],
            "valor_total": total_item,

            "criado_em": now(),
        })

    validar_transicao_contrato(
        contrato["status"],
        StatusContrato.ATIVO
    )

    # 🔓 Ativação do contrato
    contrato.update({
        "status": StatusContrato.ATIVO,
        "numero_contrato": numero_documento,
        "data_inicio": data_inicio,
        "data_fim": data_fim,

        "valor_total": valor_total,
        "valor_empenhado": 0.0,
        "valor_a_empenhar": valor_total,

        "atualizado_em": now(),
        "ativado_por": usuario,
    })

    db["contrato_itens"].extend(contrato_itens)

    return {
        "contrato": contrato,
        "itens": contrato_itens,
    }

def registrar_empenho(
    numero_empenho: str,
    contrato_id: str,
    numero_processo: str,
    uasg: str,
    orgao_gerenciador: str,
    itens: list,
    usuario: str,
):
    # 🔒 Bloqueio de duplicidade 
    if any(e["numero_empenho"] == numero_empenho for e in db["empenhos"]):
        raise ValueError("Número de empenho já registrado.")

    contrato = next(
        (c for c in db["contratos"] if c["id"] == contrato_id),
        None
    )

    if not contrato or contrato["status"] != StatusContrato.ATIVO:
        raise ValueError("Contrato inválido ou não ativo.")

    empenho_id = str(uuid.uuid4())[:8]
    valor_total = 0.0

    # =========================
    # LOOP DOS ITENS
    # =========================
    for item in itens:
        contrato_item = next(
            (ci for ci in db["contrato_itens"] if ci["id"] == item["contrato_item_id"]),
            None
        )

        if not contrato_item:
            raise ValueError("Item de contrato não encontrado.")

        saldo_disponivel = (
            contrato_item["quantidade_total"]
            - contrato_item["quantidade_empenhada"]
        )

        if item["quantidade"] > saldo_disponivel:
            raise ValueError("Quantidade empenhada excede saldo disponível.")

        valor_item = item["quantidade"] * contrato_item["valor_unitario"]
        valor_total += valor_item

        contrato_item["quantidade_empenhada"] += item["quantidade"]

        db["empenho_itens"].append({
            "id": str(uuid.uuid4())[:8],
            "empenho_id": empenho_id,
            "contrato_item_id": contrato_item["id"],
            "quantidade_empenhada": item["quantidade"],
            "valor_unitario": contrato_item["valor_unitario"],
            "valor_total": valor_item,
            "criado_em": now(),
        })

    # =========================
    # 👇 APÓS O LOOP (AQUI!)
    # =========================
    contrato["valor_empenhado"] += valor_total
    contrato["valor_a_empenhar"] -= valor_total
    contrato["atualizado_em"] = now()

    db["empenhos"].append({
        "id": empenho_id,
        "numero_empenho": numero_empenho,
        "contrato_id": contrato_id,
        "oportunidade_id": contrato["oportunidade_id"],
        "numero_processo": numero_processo,
        "uasg": uasg,
        "orgao_gerenciador": orgao_gerenciador,
        "valor_total_empenhado": valor_total,
        "data_empenho": now(),
        "usuario": usuario,
        "criado_em": now(),
    })

    # 🔚 Encerramento automático
    if all(
        ci["quantidade_empenhada"] >= ci["quantidade_total"]
        for ci in db["contrato_itens"]
        if ci["contrato_id"] == contrato_id
    ):
        validar_transicao_contrato(
            contrato["status"],
            StatusContrato.ENCERRADO
        )

        contrato["status"] = StatusContrato.ENCERRADO
        contrato["atualizado_em"] = now()

    return {
        "empenho_id": empenho_id,
        "valor_total": valor_total,
    }

def suspender_contrato(
    contrato_id: str,
    motivo: str,
    usuario: str,
):
    contrato = next(
        (c for c in db["contratos"] if c["id"] == contrato_id),
        None
    )

    if not contrato:
        raise ValueError("Contrato não encontrado.")

    validar_transicao_contrato(
        contrato["status"],
        StatusContrato.SUSPENSO
    )

    contrato["status"] = StatusContrato.SUSPENSO
    contrato["motivo_suspensao"] = motivo
    contrato["atualizado_em"] = now()
    contrato["suspenso_por"] = usuario

    return contrato

def cancelar_contrato(
    contrato_id: str,
    motivo: str,
    usuario: str,
):
    contrato = next(
        (c for c in db["contratos"] if c["id"] == contrato_id),
        None
    )

    if not contrato:
        raise ValueError("Contrato não encontrado.")

    validar_transicao_contrato(
        contrato["status"],
        StatusContrato.CANCELADO
    )

    contrato["status"] = StatusContrato.CANCELADO
    contrato["motivo_cancelamento"] = motivo
    contrato["atualizado_em"] = now()
    contrato["cancelado_por"] = usuario

    return contrato


