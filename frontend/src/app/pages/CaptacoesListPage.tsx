import { useEffect, useState } from "react";
import { listarCaptacoes } from "@/app/domains/captacao/services";

export function CaptacoesListPage() {
  const [captacoes, setCaptacoes] = useState<any[]>([]);

  useEffect(() => {
    listarCaptacoes().then(setCaptacoes);
  }, []);

  return (
    <div style={{ padding: 32 }}>
      <h1>Oportunidades Captadas</h1>

      <table width="100%" cellPadding={8}>
        <thead>
          <tr>
            <th>Processo</th>
            <th>UASG</th>
            <th>Órgão</th>
            <th>Portal</th>
            <th>Data da Disputa</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {captacoes.map((c) => (
            <tr key={c.id}>
              <td>{c.numero_processo}</td>
              <td>{c.uasg}</td>
              <td>{c.orgao}</td>
              <td>{c.portal}</td>
              <td>{new Date(c.data_hora_disputa).toLocaleString()}</td>
              <td>{c.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
