import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

import { obterCaptacaoPorId } from "@/app/domains/captacao/services";
import { obterTimelineCaptacao } from "@/app/domains/timeline/services";
import { obterAnalisePorOportunidade } from "@/app/domains/analiseEdital/services";

import { TimelineReadOnly } from "@/app/shared/components/TimelineReadOnly";

import type { ProcessoCaptado } from "@/app/domains/captacao/types";
import type { EventoTimeline } from "@/app/domains/timeline/types";
import type { AnaliseEdital } from "@/app/domains/analiseEdital/types";

export function CaptacaoDetalhePage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const [captacao, setCaptacao] = useState<ProcessoCaptado | null>(null);
  const [timeline, setTimeline] = useState<EventoTimeline[]>([]);
  const [analiseEdital, setAnaliseEdital] = useState<AnaliseEdital | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!id) return;

    Promise.all([
      obterCaptacaoPorId(id),
      obterTimelineCaptacao(id),
      obterAnalisePorOportunidade(id),
    ])
      .then(([captacao, eventos, analise]) => {
        setCaptacao(captacao);
        setTimeline(eventos);
        setAnaliseEdital(analise);
      })
      .catch(() => navigate("/captacao"))
      .finally(() => setLoading(false));
  }, [id, navigate]);

  if (loading) return <p>Carregando captação...</p>;
  if (!captacao) return null;

  const podeIniciarAnalise =
    captacao.status === "CAPTACAO" && !analiseEdital;

  return (
    <div style={{ padding: 32 }}>
      <h1>Captação {captacao.numero_processo}</h1>

      <section>
        <strong>Status:</strong> {captacao.status}
      </section>

      <section>
        <strong>UASG:</strong> {captacao.uasg}<br />
        <strong>Órgão:</strong> {captacao.orgao}<br />
        <strong>Portal:</strong> {captacao.portal}
      </section>

      <section>
        <h3>Itens</h3>
        <ul>
          {captacao.itens.map((item) => (
            <li key={item.numero_item}>
              Item {item.numero_item} — {item.subgrupo} — Qtd {item.quantidade}
            </li>
          ))}
        </ul>
      </section>

      {podeIniciarAnalise && (
        <section style={{ marginTop: 24 }}>
          <button
            onClick={() =>
              navigate(`/captacao/${captacao.id}/analise-edital`)
            }
          >
            Iniciar Análise de Edital
          </button>
        </section>
      )}

      {analiseEdital && (
        <section style={{ marginTop: 32 }}>
          <h3>Análise de Edital</h3>

          <p><strong>Decisão:</strong> {analiseEdital.decisao}</p>
          <p><strong>Prazo de entrega:</strong> {analiseEdital.prazo_entrega_dias} dias</p>
          <p><strong>Exige amostra:</strong> {analiseEdital.exige_amostra ? "Sim" : "Não"}</p>
          <p><strong>Permite adesão:</strong> {analiseEdital.permite_adesao ? "Sim" : "Não"}</p>

          {analiseEdital.motivo_desistencia && (
            <p>
              <strong>Motivo da desistência:</strong>{" "}
              {analiseEdital.motivo_desistencia}
            </p>
          )}
        </section>
      )}

      <section style={{ marginTop: 32 }}>
        <h3>Timeline do Processo</h3>
        <TimelineReadOnly eventos={timeline} />
      </section>

      <section style={{ marginTop: 32 }}>
        <button onClick={() => navigate("/captacao")}>
          Voltar para Captações
        </button>
      </section>
    </div>
  );
}
