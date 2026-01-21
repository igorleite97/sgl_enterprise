export const Sidebar = () => {
  const menu = [
    { label: "Dashboard", path: "/" },
    { label: "Captação", path: "/captacao" },
    { label: "Análise de Edital", path: "/analise-edital" },
  ];

  return (
    <aside>
      {menu.map((item) => (
        <div key={item.path}>{item.label}</div>
      ))}
    </aside>
  );
};
