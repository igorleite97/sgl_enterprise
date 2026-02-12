import { Outlet } from "react-router-dom";
import { Sidebar } from "./Sidebar";
import { Topbar } from "./Topbar";

export function AppLayout() {
  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <Sidebar />

      <div style={{ flex: 1 }}>
        <Topbar />
        <main style={{ padding: 24 }}>
          <Outlet />
        </main>
      </div>
    </div>
  );
}
