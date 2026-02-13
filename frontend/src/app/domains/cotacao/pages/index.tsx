import { CotacaoListPage } from "./CotacaoListPage";
import { CotacaoPageContainer } from "./CotacaoPageContainer";

export function CotacaoModulePage() {
  return (
    <div style={{ display: "grid", gridTemplateColumns: "420px 1fr", gap: 16, padding: 24 }}>
      <div>
        <CotacaoListPage />
      </div>

      <div style={{ borderLeft: "1px solid #e5e7eb", paddingLeft: 16 }}>
        <CotacaoPageContainer />
      </div>
    </div>
  );
}
