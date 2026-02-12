export function Topbar() {
  return (
    <header
      style={{
        height: 64,
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        padding: "0 20px",
        borderBottom: "1px solid #e5e7eb",
        background: "#fff",
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
        <div style={{ fontWeight: 800 }}>SGL Enterprise</div>
      </div>

      <div style={{ flex: 1, display: "flex", justifyContent: "center" }}>
        <div style={{ width: "min(760px, 100%)", position: "relative" }}>
          <input
            placeholder="Buscar editais, contratos, órgãos... (Ctrl+K)"
            style={{
              width: "100%",
              padding: "10px 12px",
              borderRadius: 12,
              border: "1px solid #e5e7eb",
              background: "#f8fafc",
              outline: "none",
            }}
          />
          <span
            style={{
              position: "absolute",
              right: 10,
              top: "50%",
              transform: "translateY(-50%)",
              fontSize: 12,
              padding: "4px 8px",
              borderRadius: 8,
              border: "1px solid #e5e7eb",
              background: "#fff",
              color: "#64748b",
            }}
          >
            Ctrl K
          </span>
        </div>
      </div>

      <div style={{ display: "flex", gap: 10, alignItems: "center" }}>
        <button style={{ border: "1px solid #e5e7eb", borderRadius: 10, padding: "8px 10px" }}>
          ⚙️
        </button>
        <div style={{ fontSize: 13, color: "#334155", fontWeight: 600 }}>João Silva</div>
      </div>
    </header>
  );
}
