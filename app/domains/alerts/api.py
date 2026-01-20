from fastapi import APIRouter
from app.db.memory import db
from datetime import datetime
from fastapi import HTTPException
from app.domains.alerts.enums import StatusAlerta
from app.domains.alerts.models import Alerta

router = APIRouter(
    prefix="/alertas",
    tags=["Alertas"],
)


@router.get("/", response_model=list[Alerta])
def listar_alertas(status: StatusAlerta = StatusAlerta.ATIVO):
    """
    Lista alertas por status (padrão: ATIVO).
    """
    return [
        alerta
        for alerta in db.get("alertas", [])
        if alerta.status == status
    ]

@router.post("/{alerta_id}/resolver", response_model=Alerta)
def resolver_alerta(alerta_id: str, usuario: str = "manual"):
    for alerta in db.get("alertas", []):
        if alerta.id == alerta_id:
            alerta.status = StatusAlerta.RESOLVIDO
            alerta.resolvido_em = datetime.utcnow()
            alerta.resolvido_por = usuario
            return alerta

    raise HTTPException(status_code=404, detail="Alerta não encontrado")