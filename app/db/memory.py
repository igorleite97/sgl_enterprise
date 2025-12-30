from datetime import datetime

def now():
    return datetime.utcnow()

db = {
    "captacoes": [],
    "disputas": [],
    "disputa_itens": [],
    "lances": [],
    "pos_pregao_itens": [],
}