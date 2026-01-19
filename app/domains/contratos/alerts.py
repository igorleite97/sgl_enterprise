def criar_alerta(tipo, referencia_id, mensagem, severidade):
    db["alertas"].append({
        "id": str(uuid.uuid4())[:8],
        "tipo": tipo,
        "referencia_id": referencia_id,
        "mensagem": mensagem,
        "severidade": severidade,
        "criado_em": now(),
        "lido": False,
    })
    
def alertar_empenhos():
    for e in db["empenhos"]:
        lead_time = calcular_lead_time(e)

        if lead_time == 5:
            criar_alerta(
                tipo="EMPENHO_PRAZO_CRITICO",
                referencia_id=e["id"],
                mensagem="Empenho com 5 dias para vencimento.",
                severidade="ALTA",
            )

        if lead_time < 0:
            criar_alerta(
                tipo="EMPENHO_ATRASADO",
                referencia_id=e["id"],
                mensagem=f"Empenho em atraso há {abs(lead_time)} dias.",
                severidade="CRITICA",
            )
