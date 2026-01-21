from app.db.memory import db


def obter_dashboard_processos():
    processos = db.get("processos", [])
    contratos = db.get("contratos", [])
    empenhos = db.get("empenhos", [])
    alertas = db.get("alertas", [])
    timeline = db.get("timeline", [])

    resultado = []

    for processo in processos:
        processo_id = processo["id"]

        contratos_proc = [
            c for c in contratos
            if c.get("oportunidade_id") == processo_id
        ]

        empenhos_proc = [
            e for e in empenhos
            if e.get("oportunidade_id") == processo_id
        ]

        alertas_proc = [
            a for a in alertas
            if a.entidade_id == processo_id
            or any(c["id"] == a.entidade_id for c in contratos_proc)
        ]

        eventos_proc = [
            e for e in timeline
            if e.get("context_id") == processo_id
        ][-5:]

        valor_contratado = sum(
            c.get("valor_total", 0) for c in contratos_proc
        )

        valor_empenhado = sum(
            e.get("valor_total_empenhado", 0) for e in empenhos_proc
        )

        resultado.append({
            "processo_id": processo_id,
            "numero_processo": processo.get("numero_processo"),
            "orgao": processo.get("orgao"),
            "etapas": {
                "captacao": processo.get("captacao_status"),
                "analise_edital": processo.get("analise_edital_status"),
                "cotacao": processo.get("cotacao_status"),
                "disputa": processo.get("disputa_status"),
                "pos_pregao": processo.get("pos_pregao_status"),
                "contrato": (
                    contratos_proc[-1]["status"]
                    if contratos_proc else None
                ),
            },
            "financeiro": {
                "valor_contratado": valor_contratado,
                "valor_empenhado": valor_empenhado,
                "valor_a_empenhar": valor_contratado - valor_empenhado,
            },
            "alertas": [
                {
                    "tipo": a.tipo,
                    "mensagem": a.mensagem,
                }
                for a in alertas_proc
            ],
            "timeline": eventos_proc,
        })

    return resultado
