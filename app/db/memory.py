from datetime import datetime


def now():
    return datetime.utcnow()


db = {
    "captacoes": [],
    "oportunidades": [],

    "disputas": [],
    "disputa_itens": [],
    "lances": [],

    "pos_pregao": [],
    "pos_pregao_itens": [],

    "timeline": [],
}
