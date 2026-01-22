import { useState } from "react";
import { useAuth } from "../auth/AuthContext";
import { registrarCaptacao } from "@/app/domains/captacao/services";
import { ItemCaptado, type CaptacaoInput, type PortalCompras } from "@/app/domains/captacao/types";

export function CaptacaoPage() {
  const { user } = useAuth();

  const [numeroProcesso, setNumeroProcesso] = useState("");
  const [uasg, setUasg] = useState("");
  const [orgao, setOrgao] = useState("");
  const [portal, setPortal] = useState<PortalCompras | null>(null);
  const [dataHoraDisputa, setDataHoraDisputa] = useState("");
  const [loading, setLoading] = useState(false);

  const [itens, setItens] = useState<ItemCaptado[]>([]);

  function adicionarItem() {
  setItens((prev) => [
    ...prev,
    {
      numero_item: "",
      subgrupo: "",
      valor_referencia: null,
      quantidade: 1,
    },
  ]);
}

function removerItem(index: number) {
  setItens((prev) => prev.filter((_, i) => i !== index));
}

  function handleSubmit() {
  if (!user) return;

  // 🔒 Validação mínima de UI
  if (itens.length === 0) {
    alert("Informe ao menos um item licitado");
    return;
  }

  for (const item of itens) {
    if (!item.numero_item || !item.subgrupo || !item.quantidade) {
      alert(
        "Todos os itens devem conter número do item, subgrupo e quantidade"
      );
      return;
    }
  }

  const payload: CaptacaoInput = {
    numero_processo: numeroProcesso,
    uasg,
    orgao,
    portal: portal as "COMPRASNET" | "COMPRAS_PUBLICAS",
    data_hora_disputa: dataHoraDisputa,
    itens,
  };

  // chamada real ao backend
}


  return (
    <div style={{ padding: 32 }}>
      <h1>Captação de Oportunidade</h1>

      <p style={{ color: "#374151", marginBottom: 24 }}>
        Usuário: <strong>{user?.nome}</strong> — Perfil:{" "}
        <strong>{user?.role}</strong>
      </p>

      <form
        onSubmit={handleSubmit}
        style={{
          maxWidth: 600,
          display: "flex",
          flexDirection: "column",
          gap: 12,
        }}
      >
        <input
          placeholder="Número do Processo (ex: 90084/2026)"
          value={numeroProcesso}
          onChange={(e) => setNumeroProcesso(e.target.value)}
          required
        />

        <input
          placeholder="UASG (ex: 415474)"
          value={uasg}
          onChange={(e) => setUasg(e.target.value)}
          required
        />

        <input
          placeholder="Órgão (ex: PMSP)"
          value={orgao}
          onChange={(e) => setOrgao(e.target.value)}
          required

        />

        <label>
          Portal de Compras
          <select
            value={portal ?? ""}
            onChange={(e) =>
              setPortal(e.target.value as PortalCompras)
            }
            required
          >
            <option value="">Selecione...</option>
            <option value="COMPRASNET">ComprasNet</option>
            <option value="COMPRAS_PUBLICAS">Compras Públicas</option>
          </select>
        </label>

        <input
          type="datetime-local"
          value={dataHoraDisputa}
          onChange={(e) => setDataHoraDisputa(e.target.value)}
          required
        />

<h3>Itens Licitados</h3>

{itens.map((item, index) => (
  <div
    key={index}
    style={{
      border: "1px solid #e5e7eb",
      padding: 12,
      borderRadius: 6,
    }}
  >
    <input
      placeholder="Número do Item"
      value={item.numero_item}
      onChange={(e) => {
        const copia = [...itens];
        copia[index].numero_item = e.target.value;
        setItens(copia);
      }}
      required
    />

    <input
      placeholder="Subgrupo (ex: Notebook)"
      value={item.subgrupo}
      onChange={(e) => {
        const copia = [...itens];
        copia[index].subgrupo = e.target.value;
        setItens(copia);
      }}
      required
    />

    <input
      type="number"
      placeholder="Valor de Referência (opcional)"
      value={item.valor_referencia ?? ""}
      onChange={(e) => {
        const copia = [...itens];
        copia[index].valor_referencia = e.target.value
          ? Number(e.target.value)
          : null;
        setItens(copia);
      }}
    />

    <input
      type="number"
      placeholder="Quantidade"
      value={item.quantidade}
      onChange={(e) => {
        const copia = [...itens];
        copia[index].quantidade = Number(e.target.value);
        setItens(copia);
      }}
      required
    />

    <button type="button" onClick={() => removerItem(index)}>
      Remover Item
    </button>
  </div>
))}

<button type="button" onClick={adicionarItem}>
  + Adicionar Item
</button>

        <button type="submit" disabled={loading}>
          {loading ? "Registrando..." : "Registrar Captação"}

        </button>
      </form>
    </div>
  );
}
