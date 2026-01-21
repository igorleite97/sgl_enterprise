from fastapi import APIRouter
from app.domains.dashboard.services import obter_dashboard_contratos
from app.domains.dashboard.process_services import obter_dashboard_processos


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)

@router.get("/processos")
def dashboard_processos():
    return obter_dashboard_processos()

@router.get("/contratos")
def dashboard_contratos():
    return obter_dashboard_contratos()