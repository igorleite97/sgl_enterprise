from datetime import datetime


def now():
    return datetime.utcnow().isoformat()


db = {
    "oportunidades": [],
    "oportunidades_itens": {},   # itens por oportunidade
    "analises_edital": [],
    "cotacoes": [],
    "contratos": [],
    "compras": []
}
