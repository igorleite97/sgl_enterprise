import uuid
from fastapi import HTTPException

from app.db.memory import db, now
from app.core.enums import StatusProcesso
from app.domains.analise_edital.models import (
    AnaliseEditalCreate,
    AnaliseEdital,
)
from app.domains.timeline.services import registrar_evento_timeline
from app.domains.timeline.enums import TipoEventoTimeline, SeveridadeEvento


# =========================================================
# 🔁 ALTERAÇÃO DE STATUS DO PROCESSO (OPORTUNIDADE)
# =========================================================
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


# =========================================================
# 🧾 CRIAÇÃO DA ANÁLISE DE EDITAL
# =========================================================
def criar_analise_edital(
    data: AnaliseEditalCreate,
    usuario: str,
) -> AnaliseEdital:

    oportunidade = next(
        (o for o in db["oportunidades"] if o["id"] == data.oportunidade_id),
        None,
    )

    if not oportunidade:
        raise HTTPException(status_code=404, detail="Oportunidade não encontrada")

    if data.decisao == "DESISTIR" and not data.motivo_desistencia:
        raise HTTPException(
            status_code=400,
            detail="Motivo da desistência é obrigatório quando a decisão for DESISTIR",
        )

    analise = AnaliseEdital(
        id=str(uuid.uuid4())[:8],
        oportunidade_id=data.oportunidade_id,
        prazo_entrega_dias=data.prazo_entrega_dias,
        exige_amostra=data.exige_amostra,
        permite_adesao=data.permite_adesao,
        exige_garantia_proposta=data.exige_garantia_proposta,
        local_entrega=data.local_entrega,
        observacoes=data.observacoes,
        decisao=data.decisao,
        motivo_desistencia=data.motivo_desistencia,
        status=StatusProcesso.ANALISE_INICIADA,
        criado_em=now(),
    )

    db["analises_edital"].append(analise)

    # 📌 Evento de criação
    registrar_evento_timeline(
        entidade="ANALISE_EDITAL",
        entidade_id=analise.id,
        tipo_evento=TipoEventoTimeline.CRIACAO,
        descricao="Análise de edital criada.",
        severidade=SeveridadeEvento.INFO,
        usuario=usuario,
    )

    # =====================================================
    # 🔀 DECISÃO DA ANÁLISE
    # =====================================================
    if data.decisao == "DESISTIR":
        alterar_status_analise_edital(
            analise,
            StatusProcesso.DESISTENCIA,
            usuario,
            data.motivo_desistencia,
        )

        alterar_status_processo(
            oportunidade,
            StatusProcesso.DESISTENCIA,
            usuario,
            "Desistência na análise de edital.",
        )

    else:
        alterar_status_analise_edital(
            analise,
            StatusProcesso.ANALISE_APROVADA,
            usuario,
            "Edital aprovado para continuidade.",
        )

        alterar_status_processo(
            oportunidade,
            StatusProcesso.ANALISE_EDITAL,
            usuario,
            "Processo aprovado na análise de edital.",
        )

    return analise


# =========================================================
# 🔍 CONSULTAS
# =========================================================
def obter_analise(analise_id: str) -> AnaliseEdital:
    analise = next(
        (a for a in db["analises_edital"] if a.id == analise_id),
        None,
    )

    if not analise:
        raise HTTPException(status_code=404, detail="Análise não encontrada")

    return analise


def listar_por_oportunidade(oportunidade_id: str) -> list[AnaliseEdital]:
    return [
        a for a in db["analises_edital"]
        if a.oportunidade_id == oportunidade_id
    ]


# =========================================================
# 🔄 ALTERAÇÃO DE STATUS DA ANÁLISE
# =========================================================
def alterar_status_analise_edital(
    analise: AnaliseEdital,
    novo_status: StatusProcesso,
    usuario: str,
    justificativa: str | None = None,
) -> None:

    status_anterior = analise.status

    if status_anterior == novo_status:
        raise ValueError("A análise de edital já está neste status.")

    analise.status = novo_status
    analise.atualizada_em = now()

    descricao = (
        f"Status da análise de edital alterado de {status_anterior.value} "
        f"para {novo_status.value}."
    )

    if justificativa:
        descricao += f" Justificativa: {justificativa}"

    registrar_evento_timeline(
        entidade="ANALISE_EDITAL",
        entidade_id=analise.id,
        tipo_evento=TipoEventoTimeline.STATUS,
        descricao=descricao,
        severidade=SeveridadeEvento.INFO,
        usuario=usuario,
    )
