from app.domains.timeline.enums import TipoEventoTimeline, SeveridadeEvento


REGRAS_TIMELINE = {
    TipoEventoTimeline.CRIACAO: {
        "severidade_padrao": SeveridadeEvento.BAIXA,
    },
    TipoEventoTimeline.STATUS: {
        "severidade_padrao": SeveridadeEvento.BAIXA,
    },
    TipoEventoTimeline.DECISAO: {
        "severidade_padrao": SeveridadeEvento.ALTA,
    },
    TipoEventoTimeline.OBSERVACAO: {
        "severidade_padrao": SeveridadeEvento.BAIXA,
    },
}


def resolver_severidade(tipo_evento: TipoEventoTimeline) -> SeveridadeEvento:
    regra = REGRAS_TIMELINE.get(tipo_evento)
    if not regra:
        return SeveridadeEvento.BAIXA

    return regra["severidade_padrao"]
