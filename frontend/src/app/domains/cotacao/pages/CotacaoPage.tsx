type ProcessoCotacao = {
  id: string;
  numero: string;
  orgao: string;
  uasg?: string;
  status: "EM_COTACAO" | "PENDENTE";
  itens: Array<{
    id: string;
    numero: number;
    descricao: string;
    qtd: number;
    un: string;
    estimado_unit: number;
  }>;
};

function brl(value: number) {
  return value.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}

export function CotacaoPage({ processo }: { processo: ProcessoCotacao }) {
  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", gap: 12, marginBottom: 12 }}>
        <div>
          <h1 style={{ margin: 0 }}>Cotação</h1>
          <div style={{ color: "#6b7280", fontSize: 13 }}>
            {processo.numero} • {processo.orgao} {processo.uasg ? `• UASG ${processo.uasg}` : ""}
          </div>
        </div>

        <div style={{ display: "flex", gap: 10, alignItems: "center" }}>
          <button
            style={{
              border: "1px solid #e5e7eb",
              background: "#fff",
              borderRadius: 10,
              padding: "10px 12px",
              cursor: "pointer",
              fontWeight: 700,
            }}
          >
            Recalcular
          </button>

          <button
            style={{
              border: "1px solid #2563eb",
              background: "#2563eb",
              color: "#fff",
              borderRadius: 10,
              padding: "10px 12px",
              cursor: "pointer",
              fontWeight: 800,
            }}
          >
            Salvar Cotação
          </button>
        </div>
      </div>

      <div style={{ borderTop: "1px solid #e5e7eb", paddingTop: 14 }}>
        <h3 style={{ margin: "0 0 10px" }}>Itens</h3>

        <div style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ textAlign: "left", borderBottom: "1px solid #e5e7eb" }}>
                <th style={{ padding: "10px 8px" }}>Item</th>
                <th style={{ padding: "10px 8px" }}>Qtd</th>
                <th style={{ padding: "10px 8px" }}>Un</th>
                <th style={{ padding: "10px 8px" }}>Estimado (unit)</th>
                <th style={{ padding: "10px 8px" }}>Estimado (total)</th>
                <th style={{ padding: "10px 8px" }}>Produto (nosso)</th>
                <th style={{ padding: "10px 8px" }}>Preço cotado (unit)</th>
              </tr>
            </thead>
            <tbody>
              {processo.itens.map((it) => {
                const totalEstimado = it.qtd * it.estimado_unit;
                return (
                  <tr key={it.id} style={{ borderBottom: "1px solid #f1f5f9" }}>
                    <td style={{ padding: "10px 8px" }}>
                      <div style={{ fontWeight: 700 }}>
                        {it.numero}. {it.descricao}
                      </div>
                    </td>
                    <td style={{ padding: "10px 8px" }}>{it.qtd}</td>
                    <td style={{ padding: "10px 8px" }}>{it.un}</td>
                    <td style={{ padding: "10px 8px" }}>{brl(it.estimado_unit)}</td>
                    <td style={{ padding: "10px 8px" }}>{brl(totalEstimado)}</td>

                    {/* placeholder: em breve vai virar select/autocomplete */}
                    <td style={{ padding: "10px 8px", color: "#6b7280" }}>—</td>

                    {/* placeholder: em breve vai virar input */}
                    <td style={{ padding: "10px 8px", color: "#6b7280" }}>—</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
