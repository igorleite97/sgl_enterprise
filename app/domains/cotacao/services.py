import uuid
from fastapi import HTTPException
from app.db.memory import db, now
from app.domains.cotacao.models import CotacaoCreate, CotacaoOut, StatusCotacaoItem
from app.core.enums import StatusAnaliseEdital


def _obter_ultima_analise(oportunidade_id: str):
    analises = [
        a for a in db["analises_edital"]
        if a["oportunidade_id"] == oportunidade_id
    ]
    return analises[-1] if analises else None


def criar_cotacao(data: CotacaoCreate) -> CotacaoOut:
    # 1. Validar existência da análise de edital
    analise = _obter_ultima_analise(data.oportunidade_id)

    if not analise:
        raise HTTPException(
            status_code=400,
            detail="Cotação bloqueada: oportunidade sem análise de edital."
        )

    # 2. Validar status da análise
    if analise["status"] != StatusAnaliseEdital.APROVADA:
        raise HTTPException(
            status_code=400,
            detail=f"Cotação bloqueada: análise de edital está '{analise['status']}'."
        )

    # 3. Validar desistência do item
    if data.status == StatusCotacaoItem.DESISTIDO and not data.justificativa_desistencia:
        raise HTTPException(
            status_code=400,
            detail="Desistência exige justificativa formal."
        )

    # 4. Criar cotação
    cotacao = {
        "id": str(uuid.uuid4())[:8],
        **data.model_dump(),
        "criado_em": now(),
    }

    db["cotacoes"].append(cotacao)
    return CotacaoOut(**cotacao)


def listar_por_oportunidade(oportunidade_id: str):
    return [
        c for c in db["cotacoes"]
        if c["oportunidade_id"] == oportunidade_id
    ]


def listar_por_item(item_id: str):
    return [
        c for c in db["cotacoes"]
        if c["item_id"] == item_id
    ]
