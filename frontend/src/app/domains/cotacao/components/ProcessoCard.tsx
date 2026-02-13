import type { StatusProcesso } from "@/app/core/statusProcesso";
import { STATUS_LABEL } from "@/app/domains/cotacao/status";

type Props = {
  numero_processo: string;
  uasg?: string;
  orgao: string;
  portal?: string;
  modalidade?: string;
  data_hora_disputa?: string;
  status: StatusProcesso;
  itensCount: number;
  selecionado?: boolean;
  onClick: () => void;
};

function fmtDataHora(v?: string) {
  if (!v) return "—";
  const dt = new Date(v);
  return Number.isNaN(dt.getTime()) ? "—" : dt.toLocaleString("pt-BR");
}

export function ProcessoCard(props: Props) {
  const {
    numero_processo,
    uasg,
    orgao,
    portal,
    modalidade,
    data_hora_disputa,
    status,
    itensCount,
    selecionado,
    onClick,
  } = props;

  return (
    <button
      type="button"
      onClick={onClick}
      style={{
        width: "100%",
        textAlign: "left",
        border: selecionado ? "2px solid #2563eb" : "1px solid #e5e7eb",
        background: selecionado ? "rgba(37, 99, 235, 0.06)" : "#fff",
        borderRadius: 12,
        padding: 14,
        cursor: "pointer",
      }}
    >
      <div style={{ display: "flex", justifyContent: "space-between", gap: 12 }}>
        <div style={{ fontWeight: 900 }}>{numero_processo}</div>
        <div style={{ fontSize: 12, color: "#6b7280" }}>
          {STATUS_LABEL[status] ?? status}
        </div>
      </div>

      <div style={{ marginTop: 6, color: "#111827", fontWeight: 700 }}>
        {orgao}
      </div>

      <div style={{ marginTop: 8, display: "flex", flexWrap: "wrap", gap: 8 }}>
        <span style={{ fontSize: 12, color: "#6b7280" }}>
          UASG: <strong style={{ color: "#111827" }}>{uasg ?? "—"}</strong>
        </span>

        <span style={{ fontSize: 12, color: "#6b7280" }}>
          Portal: <strong style={{ color: "#111827" }}>{portal ?? "—"}</strong>
        </span>

        <span style={{ fontSize: 12, color: "#6b7280" }}>
          Modalidade:{" "}
          <strong style={{ color: "#111827" }}>{modalidade ?? "—"}</strong>
        </span>

        <span style={{ fontSize: 12, color: "#6b7280" }}>
          Disputa:{" "}
          <strong style={{ color: "#111827" }}>
            {fmtDataHora(data_hora_disputa)}
          </strong>
        </span>
      </div>

      <div style={{ marginTop: 10, display: "flex", gap: 8 }}>
        <span
          style={{
            fontSize: 12,
            padding: "4px 8px",
            borderRadius: 999,
            background: "#f3f4f6",
            color: "#111827",
            fontWeight: 800,
          }}
        >
          {itensCount} item(ns)
        </span>
      </div>
    </button>
  );
}
