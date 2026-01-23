import { useNavigate } from "react-router-dom";

import { registrarCaptacao } from "../domains/captacao/services";
import type { CaptacaoInput } from "../domains/captacao/types";

export function NovaCaptacaoPage() {
  const navigate = useNavigate();

  const handleSubmit = async (payload: CaptacaoInput) => {
    try {
      const processo = await registrarCaptacao(payload);
      navigate(`/captacao/${processo.id}`);
    } catch (error: any) {
      if (error.tipo === "CAPTACAO_DUPLICADA") {
        alert(
          `${error.mensagem}\n\nVocê será redirecionado para a oportunidade existente.`
        );
        navigate(`/captacao/${error.processoId}`);
        return;
      }

      alert("Erro inesperado ao registrar captação.");
    }
  };

  return (
    <div>
      {/* formulário de captação */}
    </div>
  );
}
