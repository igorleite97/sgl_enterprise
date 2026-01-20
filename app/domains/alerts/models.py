from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.domains.alerts.enums import TipoAlerta, StatusAlerta


class Alerta(BaseModel):
    id: str
    tipo: TipoAlerta
    entidade: str
    entidade_id: str
    mensagem: str

    status: StatusAlerta = StatusAlerta.ATIVO

    criado_em: datetime
    resolvido_em: Optional[datetime] = None
    resolvido_por: Optional[str] = None
