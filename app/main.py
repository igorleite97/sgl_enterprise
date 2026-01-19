from fastapi import FastAPI

from app.domains.captacao.api import router as captacao_router
from app.domains.analise_edital.api import router as analise_edital_router
from app.domains.cotacao.api import router as cotacao_router
from app.domains.disputa.api import router as disputa_router
from app.domains.pos_pregao.api import router as pos_pregao_router
from app.domains.contratos.api import router as contratos_router
from app.domains.contratos.empenhos_api import router as empenhos_router
from app.domains.timeline.api import router as timeline_router
from app.domains.alerts.api import router as alerts_router


app = FastAPI(title="SGL Enterprise")

app.include_router(captacao_router, tags=["Captação"])
app.include_router(analise_edital_router, tags=["Análise de Edital"])
app.include_router(cotacao_router, tags=["Cotação"])
app.include_router(disputa_router, tags=["Disputa"])
app.include_router(pos_pregao_router, tags=["Pós-Pregão"])
app.include_router(contratos_router, tags=["Contratos"])
app.include_router(empenhos_router, tags=["Empenhos"])
app.include_router(timeline_router, tags=["Timeline"])
app.include_router(alerts_router, tags=["Alertas"])
