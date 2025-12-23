# app/domains/captacao/services.py

import uuid
from app.db.memory import db, now
from app.core.enums import StatusProcesso
from app.domains.captacao.models import CaptacaoInput, ProcessoCaptado


def registrar_captacao(data: CaptacaoInput) -> ProcessoCaptado:
    processo_id = str(uuid.uuid4())[:8]

    processo = {
        "id": processo_id,
        "numero_processo": data.numero_processo,
        "uasg": data.uasg,
        "orgao": data.orgao,
        "portal": data.portal,
        "data_hora_disputa": data.data_hora_disputa,
        "status": StatusProcesso.CAPTACAO,
        "criado_em": now(),
        "itens": []
    }

    for item in data.itens:
        processo["itens"].append(item.model_dump())

    # salva no "banco"
    db["oportunidades"].append(processo)

    return ProcessoCaptado(**processo)
