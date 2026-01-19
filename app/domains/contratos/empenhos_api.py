from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

from app.domains.contratos.services import registrar_empenho

router = APIRouter(
    prefix="/empenhos",
    tags=["Empenhos"],
)

# ============================
# SCHEMAS
# ============================

class EmpenhoItemRequest(BaseModel):
    contrato_item_id: str
    quantidade: int


class RegistrarEmpenhoRequest(BaseModel):
    numero_empenho: str
    contrato_id: str
    numero_processo: str
    uasg: str
    orgao_gerenciador: str
    data_recebimento: datetime
    itens: list[EmpenhoItemRequest]


# ============================
# ENDPOINT
# ============================

@router.post("/registrar", summary="Registrar empenho no contrato")
def api_registrar_empenho(payload: RegistrarEmpenhoRequest):
    try:
        return registrar_empenho(
            numero_empenho=payload.numero_empenho,
            contrato_id=payload.contrato_id,
            numero_processo=payload.numero_processo,
            uasg=payload.uasg,
            orgao_gerenciador=payload.orgao_gerenciador,
            itens=[i.dict() for i in payload.itens],
            usuario="api",
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
