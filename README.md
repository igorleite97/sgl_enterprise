SGL Enterprise

Sistema de Gestão de Licitações – Arquitetura Orientada a Domínio

Visão Geral

O SGL Enterprise é uma plataforma corporativa para gestão integral do ciclo de licitações, desde a captação de oportunidades até o pós-pregão, com foco em governança, rastreabilidade, tomada de decisão orientada a risco e auditoria completa do processo.

O sistema foi concebido para refletir fielmente a realidade operacional de empresas que atuam em licitações públicas, tratando cada etapa como um domínio de negócio independente, porém integrado.

Princípios Arquiteturais

Arquitetura Orientada a Domínio (DDD)
Cada fase do processo licitatório é modelada como um domínio explícito.

Separação clara de responsabilidades
APIs, serviços, modelos, enums e regras de negócio são isolados por domínio.

Auditoria transversal (Timeline)
Todas as decisões relevantes e mudanças de estado são registradas de forma cronológica, auditável e rastreável.

Decisão no nível correto
Especial atenção à Disputa por Item, onde preço, markup e risco realmente existem.

Domínios Implementados
📌 Captação

Responsável pela identificação e registro de oportunidades de licitação.

📄 Análise de Edital

Avaliação técnica, jurídica e operacional dos editais captados.

💰 Cotação

Estruturação de custos, preços e margens por item.

⚔️ Disputa

Gestão da fase competitiva da licitação, incluindo:

Disputa por item

Controle de markup mínimo

Exceções condicionadas ao perfil do usuário

Registro de lances

🕒 Timeline (Auditoria)

Domínio transversal responsável por:

Registro cronológico de eventos

Origem do evento (usuário, sistema, regra automática)

Tipo de decisão

Base para compliance, auditoria e rastreabilidade completa

📦 Pós-Pregão

Encerramento da disputa e preparação para etapas posteriores (contratação, execução, etc.).

Estado Atual do Projeto

Estrutura base consolidada

Domínios principais implementados

Timeline funcional e integrada aos eventos de negócio

Regras críticas (markup mínimo, exceções, perfis) aplicadas no domínio correto

API FastAPI estruturada por domínio

Status estimado de maturidade:
≈ 60% concluído

Próximos Passos Planejados

🔐 Padronização de eventos automáticos de mudança de status
(toda transição de fase gera evento na Timeline)

🔄 Orquestração explícita do fluxo entre domínios

🧠 Consolidação de regras de negócio como políticas reutilizáveis

📊 Endpoints avançados de consulta da Timeline (filtros, ordenação, entidade, origem)

🔒 Camada de autenticação e autorização

🧪 Testes automatizados por domínio

Tecnologias Utilizadas

Python 3.12+

FastAPI

Arquitetura modular orientada a domínio

Persistência em memória (fase inicial)

Preparado para futura integração com banco relacional

Objetivo Estratégico

O SGL Enterprise não é apenas um sistema operacional, mas uma plataforma de decisão, capaz de oferecer:

Segurança jurídica e operacional

Transparência total do processo

Base sólida para crescimento, compliance e auditoria
