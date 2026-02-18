# SGL Enterprise — Sistema de Gestão de Licitações
### Enterprise Procurement ERP Platform

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.12+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-green)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue)
![React](https://img.shields.io/badge/React-18+-61DAFB)

> **Plataforma corporativa end-to-end para gestão do ciclo completo de licitações públicas, com governança, rastreabilidade e auditoria imutável conforme Lei 14.133/21.**

---

##  Visão Geral

O **SGL Enterprise** é um ERP especializado em processos licitatórios que implementa:

✅ **Funil completo:** Captação → Análise → Cotação → Disputa → Pós-Pregão → Contratos → Empenhos  
✅ **Decisão granular:** Markup, preço real e margem calculados por item (sem distorções por médias)  
✅ **Governança corporativa:** RBAC + fluxos de aprovação com regras de exceção controladas  
✅ **Audit-by-design:** Timeline transversal com eventos de negócio imutáveis (Event Sourcing)

---

##  Arquitetura

### **Princípios de Design**

- **Domain-Driven Design (DDD):** Bounded Contexts para isolamento de regras por domínio
- **Clean Architecture:** Separação rigorosa de responsabilidades (SoC)
  - **APIs:** Rotas, autenticação, serialização
  - **Application Services:** Orquestração de fluxos e transições de estado
  - **Domain:** Invariantes e regras críticas (`rules.py`, `services.py`)

### **Regra de Ouro**

> Toda transição de estado: **valida domínio** → **persiste** → **emite evento para Timeline**

---

##  Stack Tecnológica

### **Backend**
- **Linguagem:** Python 3.12+
- **Framework:** FastAPI (async)
- **Arquitetura:** DDD + Clean Architecture
- **Persistência:** Repositórios in-memory (prontos para SQLAlchemy/PostgreSQL)
- **Auditoria:** Event Sourcing Timeline
- **Testes:** Pytest (unit + integration)

### **Frontend** *(em desenvolvimento)*
- **Framework:** React 18
- **Linguagem:** TypeScript 5.0+
- **Styling:** Tailwind CSS
- **HTTP Client:** Axios + React Query
- **State Management:** Context API

---

##  Estrutura do Projeto
```
sgl_enterprise/
├── app/                          # Backend (FastAPI)
│   ├── api/                      # Rotas e endpoints REST
│   ├── application/              # Use cases e orquestração
│   ├── domain/                   # Regras de negócio e entidades
│   │   ├── captacao/            # Bounded Context: Captação
│   │   ├── analise_edital/      # Bounded Context: Análise
│   │   ├── cotacao/             # Bounded Context: Cotação
│   │   └── ...
│   ├── infrastructure/           # Repositórios, persistência
│   └── shared/                   # Utilidades transversais
├── frontend/                     # Frontend (React + TypeScript)
│   ├── src/
│   │   ├── components/          # Componentes reutilizáveis
│   │   ├── pages/               # Páginas da aplicação
│   │   └── services/            # Integrações com API
├── tests/                        # Testes automatizados
│   ├── unit/                    # Testes unitários
│   └── integration/             # Testes de integração
├── docs/                         # Documentação técnica
├── requirements.txt              # Dependências Python
└── docker-compose.yml            # Orquestração (futuro)
```

---

##  Como Executar (Dev)

### **Pré-requisitos**
- Python 3.12+
- Node.js 18+
- npm ou yarn

### **Backend**
```bash
# Clone o repositório
git clone https://github.com/igorleite97/sgl_enterprise.git
cd sgl_enterprise

# Crie e ative ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instale dependências
pip install -r requirements.txt

# Execute o servidor
uvicorn app.main:app --reload
```

📄 **Documentação Interativa:** Acesse `http://localhost:8000/docs` (Swagger UI)

### **Frontend**
```bash
cd frontend

# Instale dependências
npm install

# Execute em modo desenvolvimento
npm run dev
```

 **Aplicação:** Acesse `http://localhost:5173`

---

##  Segurança e Compliance

- ✅ **Autenticação:** JWT com refresh tokens
- ✅ **Autorização:** RBAC (Role-Based Access Control)
- ✅ **OWASP Top 10:** Proteção contra vulnerabilidades comuns
- ✅ **LGPD:** Rastreabilidade e auditoria de dados
- ✅ **Lei 14.133/21:** Conformidade com processos licitatórios

---

##  Status do Projeto

🚧 **Em desenvolvimento ativo**

### **Implementado**
- [x] Arquitetura base (DDD + Clean Architecture)
- [x] Domínios core (Captação → Empenhos)
- [x] Timeline Service com Event Sourcing
- [x] Sistema de autenticação JWT + RBAC
- [x] Observabilidade (alertas e monitoramento)
- [x] QA (Pytest: unit + integration)
- [x] Integração API (Axios + React Query)

### **Em Desenvolvimento**
- [ ] Migração para PostgreSQL (persistência)
- [ ] Dashboard analítico (Power BI embedded)
- [ ] Integração com plataformas governamentais (ComprasNet)
- [ ] Módulo de notificações (WebSockets)
- [ ] Frontend completo (React UI)

### **Roadmap Futuro**
- [ ] Containerização completa (Docker Compose)
- [ ] CI/CD (GitHub Actions)
- [ ] Deploy em nuvem (AWS/Azure)
- [ ] Mobile app (React Native)

---

##  Testes
```bash
# Executar todos os testes
pytest

# Testes com coverage
pytest --cov=app tests/

# Apenas testes unitários
pytest tests/unit/

# Apenas testes de integração
pytest tests/integration/
```

---

## 📚 Documentação Adicional

- [Arquitetura Detalhada](docs/ARCHITECTURE.md) *(planejado)*
- [Guia de Contribuição](docs/CONTRIBUTING.md) *(planejado)*
- [Decisões de Design (ADRs)](docs/decisions/) *(planejado)*

---

##  Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

##  Autor

**Igor Leite de Andrade**

🔗 **Links:**
- LinkedIn: [linkedin.com/in/igor-leite-a9b839222](https://www.linkedin.com/in/igor-leite-a9b839222)
- GitHub: [@igorleite97](https://github.com/igorleite97)
- Email: igor_leite_123@hotmail.com

**Perfil Técnico:**
- 🎯 Desenvolvedor Backend focado em Segurança Ofensiva (Pentest / Red Team)
- 🔐 Especializado em Python, APIs REST e automação
- 🎓 Graduando em Segurança da Informação (UNIP)

---

## 🌟 Agradecimentos

Este projeto é desenvolvido com foco em aprendizado e demonstração de boas práticas de arquitetura de software, segurança e governança corporativa.

⭐ **Se este projeto foi útil de alguma forma, considere dar uma estrela!**

---

## 📞 Contato

Tem dúvidas, sugestões ou quer colaborar? Entre em contato!

- 📧 Email: igor_leite_123@hotmail.com
- 💼 LinkedIn: [Igor Leite](https://www.linkedin.com/in/igor-leite-a9b839222)
- 🐙 GitHub Issues: [Abrir uma issue](https://github.com/igorleite97/sgl_enterprise/issues)
