import { useNavigate } from "react-router-dom";

export function AnaliseEditalListPage() {
  const navigate = useNavigate();

  return (
    <div style={{ padding: 32 }}>
      <h1>Análises de Edital</h1>

      <p style={{ color: "#6b7280", marginBottom: 24 }}>
        Lista de processos aguardando ou em análise de edital.
      </p>

      {/* Placeholder controlado */}
      <div
        style={{
          border: "1px dashed #d1d5db",
          padding: 24,
          borderRadius: 8,
        }}
      >
        <p>Nenhuma análise carregada ainda.</p>

        <button
          style={{ marginTop: 16 }}
          onClick={() => navigate("/captacao")}
        >
          Ir para Captações
        </button>
      </div>
    </div>
  );
}
