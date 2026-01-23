import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

import { obterCaptacaoPorId } 
  from "@/app/domains/captacao/services";

import { obterTimelineCaptacao } 
  from "@/app/domains/timeline/services";

import { TimelineReadOnly } 
  from "@/app/shared/components/TimelineReadOnly";

import type { ProcessoCaptado } 
  from "@/app/domains/captacao/types";

import type { EventoTimeline } 
  from "@/app/domains/timeline/types";


export function CaptacaoDetalhePage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const [captacao, setCaptacao] = useState<ProcessoCaptado | null>(null);
  const [loading, setLoading] = useState(true);
  const [timeline, setTimeline] = useState<EventoTimeline[]>([]);

  useEffect(() => {
    if (!id) return;

    Promise.all([
      obterCaptacaoPorId(id),
      obterTimelineCaptacao(id),
    ])

      .then(([captacao, eventos]) => {
        setCaptacao(captacao);
        setTimeline(eventos);
      })
      .catch(() => navigate("/captacao"))
      .finally(() => setLoading(false));
  }, [id, navigate]);

  if (loading) return <p>Carregando captação...</p>;
  if (!captacao) return null;

  return (
    <div>
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

      <section>
  <h3>Timeline do Processo</h3>
  <TimelineReadOnly eventos={timeline} />
</section>

      <button onClick={() => navigate("/captacao")}>
        Voltar para Captações
      </button>
    </div>
  );
}
