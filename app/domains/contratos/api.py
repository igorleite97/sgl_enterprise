from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

from app.db.memory import db
from app.domains.contratos.services import (
    receber_contrato_ou_ata,
)

router = APIRouter(
    prefix="/contratos",
    tags=["Contratos"],
)

# ============================
# SCHEMAS
# ============================

class ReceberContratoRequest(BaseModel):
    numero_documento: str
    data_inicio: datetime
    data_fim: datetime


# ============================
# ENDPOINTS
# ============================

@router.get("/", summary="Listar contratos")
def listar_contratos():
    return db["contratos"]


@router.get("/{contrato_id}", summary="Detalhar contrato")
def detalhar_contrato(contrato_id: str):
    contrato = next(
        (c for c in db["contratos"] if c["id"] == contrato_id),
        None
    )

    if not contrato:
        raise HTTPException(status_code=404, detail="Contrato não encontrado.")

    itens = [
        i for i in db["contrato_itens"]
        if i["contrato_id"] == contrato_id
    ]

    return {
        "contrato": contrato,
        "itens": itens,
    }


@router.post(
    "/{contrato_id}/receber",
    summary="Receber contrato ou ata (ativar contrato)",
)
def api_receber_contrato(
    contrato_id: str,
    payload: ReceberContratoRequest,
):
    try:
        return receber_contrato_ou_ata(
            contrato_id=contrato_id,
            numero_documento=payload.numero_documento,
            data_inicio=payload.data_inicio,
            data_fim=payload.data_fim,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
