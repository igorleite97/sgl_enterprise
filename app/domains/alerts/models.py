from pydantic import BaseModel
from datetime import datetime
from app.domains.alerts.enums import TipoAlerta, StatusAlerta


class Alerta(BaseModel):
    id: str
    tipo: TipoAlerta
    entidade: str
    entidade_id: str
    mensagem: str
    status: StatusAlerta = StatusAlerta.ATIVO
    criado_em: datetime
