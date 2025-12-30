from app.domains.timeline.services import registrar_evento
from app.domains.timeline.enums import TipoEventoTimeline, OrigemEvento


def registrar_transicao_status(
    *,
    entidade: str,
    entidade_id: int,
    status_anterior: str,
    status_novo: str,
    origem: OrigemEvento,
    usuario: str | None = None,
    detalhe: str | None = None,
):
    descricao = (
        f"Status alterado de '{status_anterior}' para '{status_novo}'."
    )

    if detalhe:
        descricao += f" {detalhe}"

    registrar_evento(
        entidade=entidade,
        entidade_id=entidade_id,
        tipo_evento=TipoEventoTimeline.STATUS,
        descricao=descricao,
        origem=origem,
        usuario=usuario,
    )
