import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

import { criarAnaliseEdital } from "@/app/domains/analiseEdital/services";
import type { AnaliseEditalCreateInput } from "@/app/domains/analiseEdital/types";

export function AnaliseEditalPage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const [prazoEntrega, setPrazoEntrega] = useState(0);
  const [exigeAmostra, setExigeAmostra] = useState(false);
  const [permiteAdesao, setPermiteAdesao] = useState(false);
  const [exigeGarantia, setExigeGarantia] = useState(false);
  const [localEntrega, setLocalEntrega] = useState("");
  const [observacoes, setObservacoes] = useState("");

  const [decisao, setDecisao] = useState<"SEGUIR" | "DESISTIR">("SEGUIR");
  const [motivoDesistencia, setMotivoDesistencia] = useState("");

  const [loading, setLoading] = useState(false);

  function handleSubmit() {
    if (!id) return;

    if (prazoEntrega <= 0) {
      alert("Prazo de entrega deve ser maior que zero");
      return;
    }

    if (decisao === "DESISTIR" && !motivoDesistencia) {
      alert("Informe o motivo da desistência");
      return;
    }

    const payload: AnaliseEditalCreateInput = {
      oportunidade_id: id,
      prazo_entrega_dias: prazoEntrega,
      exige_amostra: exigeAmostra,
      permite_adesao: permiteAdesao,
      exige_garantia_proposta: exigeGarantia,
      local_entrega: localEntrega,
      observacoes,
      decisao,
      motivo_desistencia:
        decisao === "DESISTIR" ? motivoDesistencia : undefined,
    };

    setLoading(true);

    criarAnaliseEdital(payload)
      .then(() => {
        navigate(`/captacao/${id}`);
      })
      .finally(() => setLoading(false));
  }

  return (
    <div style={{ padding: 32, maxWidth: 600 }}>
      <h1>Análise de Edital</h1>

      <input
        type="number"
        placeholder="Prazo de entrega (dias)"
        value={prazoEntrega}
        onChange={(e) => setPrazoEntrega(Number(e.target.value))}
      />

      <label>
        <input
          type="checkbox"
          checked={exigeAmostra}
          onChange={(e) => setExigeAmostra(e.target.checked)}
        />
        Exige amostra
      </label>

      <label>
        <input
          type="checkbox"
          checked={permiteAdesao}
          onChange={(e) => setPermiteAdesao(e.target.checked)}
        />
        Permite adesão
      </label>

      <label>
        <input
          type="checkbox"
          checked={exigeGarantia}
          onChange={(e) => setExigeGarantia(e.target.checked)}
        />
        Exige garantia de proposta
      </label>

      <input
        placeholder="Local de entrega"
        value={localEntrega}
        onChange={(e) => setLocalEntrega(e.target.value)}
      />

      <textarea
        placeholder="Observações"
        value={observacoes}
        onChange={(e) => setObservacoes(e.target.value)}
      />

      <select
        value={decisao}
        onChange={(e) => setDecisao(e.target.value as any)}
      >
        <option value="SEGUIR">Seguir com o processo</option>
        <option value="DESISTIR">Desistir</option>
      </select>

      {decisao === "DESISTIR" && (
        <textarea
          placeholder="Motivo da desistência"
          value={motivoDesistencia}
          onChange={(e) => setMotivoDesistencia(e.target.value)}
        />
      )}

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Salvando..." : "Confirmar decisão"}
      </button>
    </div>
  );
}
