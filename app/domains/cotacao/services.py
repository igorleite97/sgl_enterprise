import uuid
from fastapi import HTTPException

from app.db.memory import db, now
from app.core.enums import StatusProcesso
from app.domains.cotacao.models import CotacaoCreate, Cotacao
from app.domains.timeline.services import registrar_evento_timeline
from app.domains.timeline.enums import TipoEventoTimeline, SeveridadeEvento


# ======================================================
# HELPERS DE STATUS DO PROCESSO (AUDITÁVEL)
# ======================================================
def alterar_status_processo(
    processo: dict,
    novo_status: StatusProcesso,
    usuario: str,
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

    registrar_evento_timeline(
        entidade="PROCESSO",
        entidade_id=processo["id"],
        tipo_evento=TipoEventoTimeline.STATUS,
        descricao=descricao,
        severidade=SeveridadeEvento.INFO,
        usuario=usuario,
    )


# ======================================================
# CRIAÇÃO DE COTAÇÃO
# ======================================================
def criar_cotacao(
    data: CotacaoCreate,
    usuario: str,
) -> Cotacao:

    oportunidade = next(
        (o for o in db["oportunidades"] if o["id"] == data.oportunidade_id),
        None
    )

    if not oportunidade:
        raise HTTPException(status_code=404, detail="Oportunidade não encontrada")

    if oportunidade["status"] != StatusProcesso.ANALISE_APROVADA:
        raise HTTPException(
            status_code=400,
            detail="Cotação só pode ser criada após análise de edital aprovada."
        )

    cotacao = Cotacao(
        id=str(uuid.uuid4())[:8],
        oportunidade_id=data.oportunidade_id,
        fornecedor=data.fornecedor,
        valor_total=data.valor_total,
        prazo_entrega_dias=data.prazo_entrega_dias,
        observacoes=data.observacoes,
        status=StatusProcesso.COTACAO_INICIADA,
        criado_em=now(),
    )

    db["cotacoes"].append(cotacao)

    registrar_evento_timeline(
        entidade="COTACAO",
        entidade_id=cotacao.id,
        tipo_evento=TipoEventoTimeline.CRIACAO,
        descricao="Cotação criada.",
        severidade=SeveridadeEvento.INFO,
        usuario=usuario,
    )

    alterar_status_processo(
        processo=oportunidade,
        novo_status=StatusProcesso.COTACAO,
        usuario=usuario,
        justificativa="Cotação iniciada.",
    )

    return cotacao


# ======================================================
# CONSULTAS
# ======================================================
def obter_cotacao(cotacao_id: str) -> Cotacao:
    cotacao = next(
        (c for c in db["cotacoes"] if c.id == cotacao_id),
        None
    )

    if not cotacao:
        raise HTTPException(status_code=404, detail="Cotação não encontrada")

    return cotacao


def listar_por_oportunidade(oportunidade_id: str) -> list[Cotacao]:
    return [
        c for c in db["cotacoes"]
        if c.oportunidade_id == oportunidade_id
    ]


# ======================================================
# STATUS DA COTAÇÃO
# ======================================================
def alterar_status_cotacao(
    cotacao: Cotacao,
    novo_status: StatusProcesso,
    usuario: str,
    justificativa: str | None = None,
) -> None:

    status_anterior = cotacao.status

    if status_anterior == novo_status:
        raise ValueError("A cotação já está neste status.")

    cotacao.status = novo_status
    cotacao.atualizada_em = now()

    descricao = (
        f"Status da cotação alterado de {status_anterior.value} "
        f"para {novo_status.value}."
    )

    if justificativa:
        descricao += f" Justificativa: {justificativa}"

    registrar_evento_timeline(
        entidade="COTACAO",
        entidade_id=cotacao.id,
        tipo_evento=TipoEventoTimeline.STATUS,
        descricao=descricao,
        severidade=SeveridadeEvento.INFO,
        usuario=usuario,
    )

def encerrar_cotacao(
    cotacao: Cotacao,
    usuario: str,
) -> None:

    if cotacao.status != StatusProcesso.COTACAO:
        raise ValueError("A cotação só pode ser encerrada se estiver ativa.")

    alterar_status_cotacao(
        cotacao,
        StatusProcesso.COTACAO_ENCERRADA,
        usuario,
        "Cotação finalizada com sucesso.",
    )

    oportunidade = next(
        (o for o in db["oportunidades"] if o["id"] == cotacao.oportunidade_id),
        None
    )

    if not oportunidade:
        raise ValueError("Oportunidade não encontrada para encerramento da cotação.")

    alterar_status_processo(
        oportunidade,
        StatusProcesso.DISPUTA,
        usuario,
        "Processo avançou para fase de disputa.",
    )
