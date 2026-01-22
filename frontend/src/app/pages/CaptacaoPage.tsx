import { useState } from "react";
import { useAuth } from "../auth/AuthContext";
import { registrarCaptacao } from "@/app/domains/captacao/services";
import type { CaptacaoInput, PortalCompras } from "@/app/domains/captacao/types";

export function CaptacaoPage() {
  const { user } = useAuth();

  const [numeroProcesso, setNumeroProcesso] = useState("");
  const [uasg, setUasg] = useState("");
  const [orgao, setOrgao] = useState("");
  const [portal, setPortal] = useState<PortalCompras | null>(null);
  const [dataHoraDisputa, setDataHoraDisputa] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!portal) {
  alert("Selecione o portal de compras");
  return;
}
    const payload: CaptacaoInput = {
      numero_processo: numeroProcesso,
      uasg,
      orgao,
      portal, // agora 100% compatível
      data_hora_disputa: dataHoraDisputa,
      itens: [], 
    };

    try {
      setLoading(true);
      const processo = await registrarCaptacao(payload);

      console.log("Processo criado:", processo);

      // próximo passo: navegação por ID real
      // navigate(`/captacao/${processo.id}`);
    } catch (error) {
      console.error("Erro ao registrar captação", error);
    } finally {
      setLoading(false);
    }
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

        <button type="submit" disabled={loading}>
          {loading ? "Registrando..." : "Registrar Captação"}
        </button>
      </form>
    </div>
  );
}
