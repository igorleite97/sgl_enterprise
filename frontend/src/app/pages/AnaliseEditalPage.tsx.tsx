import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

import { criarAnaliseEdital } from "@/app/domains/analiseEdital/services";
import type { AnaliseEditalCreate } from "@/app/domains/analiseEdital/types";

export function AnaliseEditalPage() {
  const { id: oportunidadeId } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const [form, setForm] = useState<AnaliseEditalCreate>({
    oportunidade_id: oportunidadeId!,
    prazo_entrega_dias: 0,
    exige_amostra: false,
    permite_adesao: false,
    exige_garantia_proposta: false,
    local_entrega: "",
    observacoes: "",
    decisao: "SEGUIR",
  });

  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState<string | null>(null);

  function atualizarCampo<K extends keyof AnaliseEditalCreate>(
    campo: K,
    valor: AnaliseEditalCreate[K]
  ) {
    setForm((prev) => ({ ...prev, [campo]: valor }));
  }

  async function handleSubmit() {
    setErro(null);

    if (form.decisao === "DESISTIR" && !form.motivo_desistencia) {
      setErro("Motivo da desistência é obrigatório.");
      return;
    }

    try {
      setLoading(true);
      await criarAnaliseEdital(form);
      navigate(`/captacao/${oportunidadeId}`);
    } catch (e) {
      setErro("Erro ao registrar análise de edital.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <h1>Análise de Edital</h1>

      {erro && <p style={{ color: "red" }}>{erro}</p>}

      <section>
        <label>
          Prazo de entrega (dias)
          <input
            type="number"
            value={form.prazo_entrega_dias}
            onChange={(e) =>
              atualizarCampo("prazo_entrega_dias", Number(e.target.value))
            }
          />
        </label>

        <label>
          Local de entrega
          <input
            type="text"
            value={form.local_entrega}
            onChange={(e) =>
              atualizarCampo("local_entrega", e.target.value)
            }
          />
        </label>

        <label>
          <input
            type="checkbox"
            checked={form.exige_amostra}
            onChange={(e) =>
              atualizarCampo("exige_amostra", e.target.checked)
            }
          />
          Exige amostra
        </label>

        <label>
          <input
            type="checkbox"
            checked={form.permite_adesao}
            onChange={(e) =>
              atualizarCampo("permite_adesao", e.target.checked)
            }
          />
          Permite adesão
        </label>

        <label>
          <input
            type="checkbox"
            checked={form.exige_garantia_proposta}
            onChange={(e) =>
              atualizarCampo("exige_garantia_proposta", e.target.checked)
            }
          />
          Exige garantia de proposta
        </label>
      </section>

      <section>
        <h3>Decisão</h3>

        <label>
          <input
            type="radio"
            checked={form.decisao === "SEGUIR"}
            onChange={() => atualizarCampo("decisao", "SEGUIR")}
          />
          Seguir com o processo
        </label>

        <label>
          <input
            type="radio"
            checked={form.decisao === "DESISTIR"}
            onChange={() => atualizarCampo("decisao", "DESISTIR")}
          />
          Desistir do processo
        </label>

        {form.decisao === "DESISTIR" && (
          <textarea
            placeholder="Motivo da desistência"
            value={form.motivo_desistencia || ""}
            onChange={(e) =>
              atualizarCampo("motivo_desistencia", e.target.value)
            }
          />
        )}
      </section>

      <button
  onClick={() =>
    navigate(`/captacao/${captacao.id}/analise-edital`)
  }
>
  Iniciar Análise de Edital
</button>
    </div>
  );
}
