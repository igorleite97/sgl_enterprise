from fastapi import APIRouter, HTTPException
from app.domains.disputa.services import iniciar_disputa

router = APIRouter(prefix="/disputa", tags=["Disputa"])


@router.post("/iniciar/{oportunidade_id}")
def iniciar(oportunidade_id: str):
    try:
        return iniciar_disputa(oportunidade_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
