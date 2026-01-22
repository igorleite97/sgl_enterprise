SGL Enterprise Sistema de Gestão de Licitações — Enterprise Procurement Resource Planning 

1. Visão Geral
O SGL Enterprise é uma solução corporativa robusta projetada para a gestão do ciclo de vida completo de licitações públicas (End-to-End Procurement). O sistema transcende o modelo de gestão operacional tradicional, posicionando-se como uma Plataforma de Decisão Estratégica.

Arquitetado para atender às rigorosas demandas da Lei 14.133/21, o projeto foca em quatro pilares fundamentais:
   - Governança Corporativa: Centralização de regras e fluxos de aprovação.
   - Rastreabilidade Assistida: Monitoramento integral de transições de estado.
   - Mitigação de Risco: Tomada de decisão baseada em dados granulares (nível de item).
   - Auditabilidade Imutável: Registro cronológico de eventos críticos (Timeline).

2. Pilares Arquiteturais

🧱 Domain-Driven Design (DDD): A estrutura do sistema é segmentada em Bounded Contexts (Contextos Delimitados), garantindo que cada fase do processo licitatório possua modelos, entidades e regras de negócio isoladas, evitando o acoplamento indevido e facilitando a manutenção evolutiva.

🔀 Separação de Responsabilidades (SoC)
    - Interface Layer (APIs): Orquestração de rotas e serialização de dados.
    - Application Services: Gerenciamento de fluxos e orquestração de transições.
    - Domain Rules: O "Coração do Negócio". Validações críticas e invariantes residem estritamente em módulos de rules.py e services.py.
    
🕒 Audit-by-Design (Timeline Transversal): Diferente de logs convencionais, a Timeline é uma implementação inspirada em Event Sourcing, onde cada alteração relevante de estado é capturada como um evento de negócio. Isso garante uma base sólida para compliance e auditorias forenses.

🎯 Granularidade de Decisão: O motor decisório opera na escala do Item. Ao isolar variáveis como markup, preço real e margem de contribuição por unidade, eliminamos distorções estatísticas comuns em análises baseadas em médias agregadas.

3. Ecossistema de Domínios
    - Captação: Ingestão e catalogação de oportunidades (UASG, Portais, Cronograma).
    - Análise de Edital: Workflow de avaliação técnica e jurídica com histórico de pareceres.
    - Cotação: Engenharia de custos e formação de preço com controle de margem de contribuição.
    - Disputa: Motor de lances em tempo real com validação de markup mínimo e perfis de exceção.
    - Pós-Pregão: Consolidação de resultados e transição para o ciclo contratual.
    - Contratos: Lifecycle Management: Ativação, suspensão e encerramento por exaustão de saldo.
    - Empenhos: Controle financeiro estrito: Validação de saldo por item e prevenção de over-spending.

4. Matriz de Maturidade do Projeto 
Backend (Python/FastAPI)

       [x] Arquitetura Base: Consolidada (DDD/Clean Arch).
         
       [x] Domínios Core: Implementados (Captação a Empenhos).
         
       [x] Timeline Service: Funcional e integrado.
         
       [ ] Observabilidade: Alertas automáticos e monitoramento de eventos.
         
       [ ] Quality Assurance: Testes unitários e de integração (Pytest).
 
Frontend (React/TypeScript)

       [x] Core Engine: Arquitetura base e Context API.
          
       [x] Auth & Session: Gestão de tokens e contexto de usuário.
         
       [x] Feature Captation: Implementada com estado controlado.
          
       [ ] API Integration: Em progresso (Axios/React Query).
    
 5. Especificações Técnicas e Invariantes
 
 🔒 Regra de Ouro (State Management)
 Toda e qualquer transição de estado no ecossistema deve, obrigatoriamente:
     1) Validar as Business Rules do domínio específico.
     2) Persistir o novo estado na camada de infraestrutura.
     3) Propagar um evento imutável para a Timeline.
     
 🛠️ Stack Tecnológica
     - Linguagem: Python 3.12+ (Typed).
     - Framework: FastAPI (Asynchronous I/O).
     - Persistência: Arquitetura desacoplada preparada para SQLAlchemy/PostgreSQL (Atual: In-memory Repository Pattern).
     - Frontend: React, TypeScript, Tailwind CSS.
     
6. Roadmap e Próximos Passos
    1) Engine de Alertas: Notificações baseadas em severidade e risco operacional.
    2) Advanced Analytics: Consultas complexas na Timeline para análise de comportamento de disputa.
    3) Security: Implementação de OAuth2/JWT com controle de acesso granular (RBAC).
    4) DevOps: Containerização via Docker e orquestração de ambiente de homologação.

Observação Profissional: Este repositório reflete um compromisso com o rigor arquitetural e a excelência técnica, desenvolvido para suportar operações corporativas reais onde a integridade dos dados e a segurança jurídica são mandatórias.
