from fastapi import APIRouter
from app.db.memory import db
from app.domains.alerts.models import Alerta

router = APIRouter(
    prefix="/alertas",
    tags=["Alertas"],
)


@router.get("/", response_model=list[Alerta])
def listar_alertas():
    """
    Lista todos os alertas gerados no sistema.
    """
    return db.get("alertas", [])
