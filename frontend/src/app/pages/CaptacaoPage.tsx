import { useState } from "react";
import { useAuth } from "../auth/AuthContext";

export function CaptacaoPage() {
  const { user } = useAuth();

  const [numeroProcesso, setNumeroProcesso] = useState("");
  const [uasg, setUasg] = useState("");
  const [orgao, setOrgao] = useState("");
  const [portal, setPortal] = useState("");
  const [dataHoraDisputa, setDataHoraDisputa] = useState("");

  return (
    <div style={{ padding: 32, maxWidth: 700 }}>
      <h1>Captação de Oportunidade</h1>

      <p style={{ color: "#374151", marginBottom: 24 }}>
        Usuário: <strong>{user?.nome}</strong> — Perfil:{" "}
        <strong>{user?.role}</strong>
      </p>

      <hr />

      <h3>Dados do Processo</h3>

      <form
        style={{
          display: "flex",
          flexDirection: "column",
          gap: 12,
          marginTop: 16,
        }}
      >
        <input
          placeholder="Número do Processo (Ex: 90084/2026)"
          value={numeroProcesso}
          onChange={(e) => setNumeroProcesso(e.target.value)}
          required
        />

        <input
          placeholder="UASG (Ex: 160474)"
          value={uasg}
          onChange={(e) => setUasg(e.target.value)}
          required
        />

        <input
          placeholder="Órgão (ex: Marinha do Brasil)"
          value={orgao}
          onChange={(e) => setOrgao(e.target.value)}
          required
        />

        <label>
          Portal de Compras
          <select
            value={portal}
            onChange={(e) => setPortal(e.target.value)}
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

        <button type="button">Finalizar Captação</button>
      </form>
    </div>
  );
}
