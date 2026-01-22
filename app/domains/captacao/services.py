import uuid

from app.db.memory import db, now
from app.core.enums import StatusProcesso
from app.domains.captacao.models import CaptacaoInput, ProcessoCaptado
from app.domains.timeline.services import registrar_evento_timeline
from app.domains.timeline.enums import TipoEventoTimeline, SeveridadeEvento
from app.domains.captacao.exceptions import ProcessoDuplicadoError
from app.domains.captacao.utils import normalizar_numero_processo
from app.db.memory import db


def registrar_captacao(
    data: CaptacaoInput,
    usuario: str,
) -> ProcessoCaptado:

    numero_processo_normalizado = normalizar_numero_processo(
        data.numero_processo
    )

    uasg_normalizada = data.uasg.strip()

    for existente in db["oportunidades"]:
        if (
            existente.uasg == uasg_normalizada
            and existente.numero_processo == numero_processo_normalizado
        ):
            raise ProcessoDuplicadoError(processo_id=existente.id)

    processo = ProcessoCaptado(
        id=str(uuid.uuid4())[:8],
        numero_processo=numero_processo_normalizado,
        uasg=uasg_normalizada,
        orgao=data.orgao.strip(),
        portal=data.portal,
        data_hora_disputa=data.data_hora_disputa,
        status=StatusProcesso.IDENTIFICADA,
        criado_em=now(),
        itens=[item.model_dump() for item in data.itens],
    )

    db["oportunidades"].append(processo)

    registrar_evento_timeline(
        entidade="CAPTACAO",
        entidade_id=processo.id,
        tipo_evento=TipoEventoTimeline.CRIACAO,
        descricao="Captação registrada no sistema.",
        severidade=SeveridadeEvento.INFO,
        usuario=usuario,
    )

    return processo

import re

def normalizar_numero_processo(numero: str) -> str:
    """
    Normaliza o número do processo para evitar duplicidade lógica.
    Ex: 90012/2026, 90012-2026, 90012 2026 -> 90012-2026
    """
    numero = numero.strip().upper()
    numero = re.sub(r"[\/\\_\s]+", "-", numero)
    return numero


def alterar_status_captacao(
    captacao: ProcessoCaptado,
    novo_status: StatusProcesso,
    usuario: str,
    justificativa: str | None = None,
) -> None:
    """
    Altera o status da captação de forma auditável.
    """

    status_anterior = captacao.status

    if status_anterior == novo_status:
        raise ValueError("A captação já está neste status.")

    captacao.status = novo_status
    captacao.atualizada_em = now()

    descricao = (
        f"Status da captação alterado de {status_anterior.value} "
        f"para {novo_status.value}."
    )

    if justificativa:
        descricao += f" Justificativa: {justificativa}"

    registrar_evento_timeline(
        entidade="CAPTACAO",
        entidade_id=captacao.id,
        tipo_evento=TipoEventoTimeline.STATUS,
        descricao=descricao,
        severidade=SeveridadeEvento.INFO,
        usuario=usuario,
    )
