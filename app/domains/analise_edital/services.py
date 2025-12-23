import uuid
from datetime import datetime
from fastapi import HTTPException

from app.db.memory import db
from app.core.enums import StatusProcesso
from app.domains.analise_edital.models import (
    AnaliseEditalCreate,
    AnaliseEdital
)


def criar_analise_edital(data: AnaliseEditalCreate) -> AnaliseEdital:
    # Verifica se a oportunidade existe
    oportunidade = next(
        (o for o in db["oportunidades"] if o["id"] == data.oportunidade_id),
        None
    )

    if not oportunidade:
        raise HTTPException(status_code=404, detail="Oportunidade não encontrada")

    # Regra obrigatória de desistência
    if data.decisao == "DESISTIR" and not data.motivo_desistencia:
        raise HTTPException(
            status_code=400,
            detail="Motivo da desistência é obrigatório quando a decisão for DESISTIR"
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
        criado_em=datetime.utcnow()
    )

    # Salva análise
    db["analises_edital"].append(analise.model_dump())

    # Atualiza status da oportunidade
    if data.decisao == "DESISTIR":
        oportunidade["status"] = StatusProcesso.DESISTENCIA
    else:
        oportunidade["status"] = StatusProcesso.ANALISE_EDITAL

    return analise


def obter_analise(analise_id: str):
    analise = next(
        (a for a in db["analises_edital"] if a["id"] == analise_id),
        None
    )
    if not analise:
        raise HTTPException(status_code=404, detail="Análise não encontrada")
    return analise


def listar_por_oportunidade(oportunidade_id: str):
    return [
        a for a in db["analises_edital"]
        if a["oportunidade_id"] == oportunidade_id
    ]
