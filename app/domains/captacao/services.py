import uuid

from app.db.memory import db, now
from app.core.enums import StatusProcesso
from app.domains.captacao.models import CaptacaoInput, ProcessoCaptado
from app.domains.timeline.services import registrar_evento_timeline
from app.domains.timeline.enums import TipoEventoTimeline, SeveridadeEvento


def registrar_captacao(
    data: CaptacaoInput,
    usuario: str,
) -> ProcessoCaptado:
    """
    Registra uma nova captação e cria o primeiro evento de auditoria.
    """

    processo = ProcessoCaptado(
        id=str(uuid.uuid4())[:8],
        numero_processo=data.numero_processo,
        uasg=data.uasg,
        orgao=data.orgao,
        portal=data.portal,
        data_hora_disputa=data.data_hora_disputa,
        status=StatusProcesso.IDENTIFICADA,
        criado_em=now(),
        itens=[item.model_dump() for item in data.itens],
    )

    db["oportunidades"].append(processo)

    # 📌 Evento inicial de auditoria
    registrar_evento_timeline(
        entidade="CAPTACAO",
        entidade_id=processo.id,
        tipo_evento=TipoEventoTimeline.CRIACAO,
        descricao="Captação registrada no sistema.",
        severidade=SeveridadeEvento.INFO,
        usuario=usuario,
    )

    return processo


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
