import uuid
from datetime import date

from app.db.memory import db, now
from app.domains.alerts.enums import TipoAlerta
from app.domains.alerts.orchestrator import alerta_ja_existe
from app.domains.alerts.rules import (
    alerta_prazo_entrega,
    alerta_saldo_baixo,
)
from app.domains.timeline.services import registrar_evento_timeline
from app.domains.timeline.enums import TipoEventoTimeline, SeveridadeEvento


def gerar_alertas_empenhos(usuario: str = "sistema"):
    from app.domains.alerts.models import Alerta
    hoje = date.today()

    for empenho in db.get("empenhos", []):
        mensagem = alerta_prazo_entrega(
            data_entrega=empenho["data_entrega_prevista"],
            hoje=hoje,
        )

        if mensagem:
            alerta = Alerta(
                id=str(uuid.uuid4())[:8],
                tipo=TipoAlerta.PRAZO_ENTREGA,
                entidade="EMPENHO",
                entidade_id=empenho["id"],
                mensagem=mensagem,
                criado_em=now(),
            )

            db.setdefault("alertas", []).append(alerta)

            registrar_evento_timeline(
                entity_type="EMPENHO",
                entity_id=empenho["id"],
                tipo_evento=TipoEventoTimeline.OBSERVACAO,
                payload={
                    "alerta": mensagem,
                    "tipo": TipoAlerta.PRAZO_ENTREGA,
                },
                severidade=SeveridadeEvento.ALTA,
                usuario=usuario,
            )


def gerar_alertas_contratos(usuario: str = "sistema"):
    from app.domains.alerts.models import Alerta
    for contrato in db.get("contratos", []):
        mensagem = alerta_saldo_baixo(
            contrato["valor_a_empenhar"]
        )

        if mensagem:
            alerta = Alerta(
                id=str(uuid.uuid4())[:8],
                tipo=TipoAlerta.SALDO_BAIXO,
                entidade="CONTRATO",
                entidade_id=contrato["id"],
                mensagem=mensagem,
                criado_em=now(),
            )

            db.setdefault("alertas", []).append(alerta)

            registrar_evento_timeline(
                entity_type="CONTRATO",
                entity_id=contrato["id"],
                tipo_evento=TipoEventoTimeline.OBSERVACAO,
                payload={
                    "alerta": mensagem,
                    "tipo": TipoAlerta.SALDO_BAIXO,
                    "valor_a_empenhar": contrato["valor_a_empenhar"],
                },
                severidade=SeveridadeEvento.CRITICA,
                usuario=usuario,
            )

