# SGL Enterprise — Sistema de Gestão de Licitações (Enterprise Procurement ERP)

O **SGL Enterprise** é uma plataforma corporativa **End-to-End** para gestão do ciclo completo de licitações públicas, projetada para ambientes que exigem **governança**, **rastreabilidade**, **mitigação de risco** e **auditabilidade imutável** (Lei 14.133/21).

## Principais Capacidades
- **Funil completo**: Captação → Análise de Edital → Cotação → Disputa → Pós-Pregão → Contratos → Empenhos
- **Decisão em nível de item**: markup, preço real e margem por unidade (sem distorções por médias)
- **Governança corporativa**: regras e fluxos de aprovação (RBAC + exceções controladas)
- **Audit-by-design**: Timeline transversal inspirada em Event Sourcing (eventos de negócio imutáveis)

## Arquitetura
- **DDD (Bounded Contexts)** para isolamento de modelos e regras por domínio
- **Clean Architecture / SoC**
  - APIs: rotas, autenticação, serialização
  - Application Services: orquestração de fluxos e transições
  - Domain: invariantes e regras críticas (`rules.py`, `services.py`)
- **Regra de Ouro**: toda transição de estado valida domínio → persiste → emite evento para Timeline

## Stack
- Backend: **Python 3.12+**, **FastAPI** (async), repositórios in-memory prontos para SQLAlchemy/PostgreSQL
- Frontend: **React**, **TypeScript**, **Tailwind CSS**

## Status do Projeto
- [x] Arquitetura Base (DDD/Clean)
- [x] Domínios Core (Captação → Empenhos)
- [x] Timeline Service integrado
- [ ] Observabilidade (alertas e monitoramento)
- [ ] QA (Pytest: unit + integration)
- [ ] Integração API (Axios/React Query)

## Como Executar (Dev)
- Backend: `uvicorn app.main:app --reload`
- Frontend: `npm install && npm run dev`
