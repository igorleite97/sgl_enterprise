from app.db.memory import db
from datetime import date


def obter_dashboard_contratos():
    contratos = db.get("contratos", [])
    alertas = db.get("alertas", [])

    contratos_vigentes = [
        c for c in contratos
        if c["status"] == "ATIVO"
    ]

    valor_total = sum(
        c.get("valor_total", 0) for c in contratos_vigentes
    )

    valor_empenhado = sum(
        c.get("valor_empenhado", 0) for c in contratos_vigentes
    )

    valor_a_empenhar = sum(
        c.get("valor_a_empenhar", 0) for c in contratos_vigentes
    )

    lista = []

    for contrato in contratos_vigentes:
        alertas_contrato = [
            a for a in alertas
            if a.entidade == "CONTRATO"
            and a.entidade_id == contrato["id"]
        ]

        lista.append({
            "id": contrato["id"],
            "numero_contrato": contrato["numero_contrato"],
            "vigencia": {
                "inicio": contrato["data_inicio"],
                "fim": contrato["data_fim"],
            },
            "valor_empenhado": contrato["valor_empenhado"],
            "valor_a_empenhar": contrato["valor_a_empenhar"],
            "status": contrato["status"],
            "alertas": [
                {
                    "tipo": a.tipo,
                    "mensagem": a.mensagem,
                }
                for a in alertas_contrato
            ],
        })

    return {
        "kpis": {
            "contratos_vigentes": len(contratos_vigentes),
            "valor_total": valor_total,
            "valor_empenhado": valor_empenhado,
            "valor_a_empenhar": valor_a_empenhar,
        },
        "contratos": lista,
    }
