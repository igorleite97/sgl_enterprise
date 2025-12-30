from fastapi import FastAPI

from app.domains.captacao.api import router as captacao_router
from app.domains.analise_edital.api import router as analise_edital_router
from app.domains.cotacao.api import router as cotacao_router
from app.domains.disputa.api import router as disputa_router
from app.domains.pos_pregao.api import router as pos_pregao_router

app = FastAPI(title="SGL Enterprise")

app.include_router(captacao_router)
app.include_router(analise_edital_router)
app.include_router(cotacao_router)
app.include_router(disputa_router)
app.include_router(pos_pregao_router)