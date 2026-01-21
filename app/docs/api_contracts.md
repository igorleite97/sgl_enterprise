# SGL Enterprise — Contrato de API (Backend)

## Princípios
- APIs são estáveis
- Read models não alteram estado
- Frontend não acessa domínios internos

---

## Dashboard

### GET /dashboard/contratos
Retorna visão agregada de contratos ativos.

Resposta:
- kpis
- lista de contratos
- alertas associados

---

### GET /dashboard/processos
Retorna visão fim-a-fim por processo.

Inclui:
- status por etapa
- financeiro consolidado
- alertas herdados
- últimos eventos da timeline

---

## Alertas

### GET /alertas
Lista alertas ativos do sistema.

---

## Timeline
(uso interno por ora)

Eventos são imutáveis.
Timeline é a base de auditoria e IA futura.
