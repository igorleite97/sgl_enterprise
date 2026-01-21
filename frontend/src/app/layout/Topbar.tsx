export const Topbar = () => {
  return (
    <header
      style={{
        height: 56,
        borderBottom: "1px solid #e5e7eb",
        padding: "0 24px",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        backgroundColor: "#ffffff",
      }}
    >
      <strong>SGL Enterprise</strong>
      <span>Usuário</span>
    </header>
  );
};
