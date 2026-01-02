# app/domains/processo/services.py

from app.db.memory import now
from app.domains.timeline.services import registrar_evento
from app.domains.timeline.enums import TipoEventoTimeline, OrigemEvento
from app.core.enums import StatusProcesso


def alterar_status_processo(
    processo: dict,
    novo_status: StatusProcesso,
    usuario: str,
    origem: OrigemEvento,
    justificativa: str | None = None,
) -> None:
    status_anterior = processo["status"]

    if status_anterior == novo_status:
        raise ValueError("O processo já está neste status.")

    processo["status"] = novo_status
    processo["atualizada_em"] = now()

    descricao = (
        f"Status do processo alterado de {status_anterior.value} "
        f"para {novo_status.value}."
    )

    if justificativa:
        descricao += f" Justificativa: {justificativa}"

    registrar_evento(
        entidade="PROCESSO",
        entidade_id=processo["id"],
        tipo_evento=TipoEventoTimeline.STATUS,
        descricao=descricao,
        origem=origem,
        usuario=usuario,
    )
