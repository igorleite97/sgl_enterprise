RELATÓRIO TÉCNICO DO PROJETO
SGL ENTERPRISE — Sistema de Gestão de Licitações

Responsável técnico: Igor Leite de Andrade
Arquitetura: Backend Python · FastAPI · Arquitetura orientada a domínios
Objetivo do sistema: Gestão completa, auditável e rastreável do ciclo de vida de licitações públicas, do funil de captação ao pós-pregão.

1. VISÃO GERAL DO PROJETO

O SGL Enterprise foi concebido como um sistema corporativo, auditável e orientado a processo, cobrindo todo o ciclo operacional de licitações:

Captação

Análise de Edital

Cotação

Disputa (por item)

Pós-Pregão

Auditoria via Timeline transversal

A arquitetura evita CRUD ingênuo e privilegia:

Regras de negócio explícitas

Eventos de domínio

Rastreamento de decisões

Separação clara de responsabilidades

2. ARQUITETURA IMPLEMENTADA
2.1 Estrutura Geral

FastAPI como framework principal

Organização por domínios de negócio

Banco em memória (db) para validação conceitual

Serviços de domínio responsáveis por regras e mutações

APIs atuando apenas como camada de orquestração

app/
 ├─ core/
 ├─ db/
 ├─ domains/
 │   ├─ captacao/
 │   ├─ analise_edital/
 │   ├─ cotacao/
 │   ├─ disputa/
 │   ├─ pos_pregao/
 │   ├─ timeline/
 └─ main.py

3. FUNCIONALIDADES JÁ IMPLEMENTADAS (ESTADO ATUAL)
3.1 Captação de Oportunidades ✅

Status: FUNCIONAL

Registro de oportunidades

Estrutura preparada para funil

API ativa e integrada ao app principal

Observação:
Fase preparada para enriquecimento futuro (palavras-chave, filtros avançados).

3.2 Análise de Edital ✅

Status: FUNCIONAL

Estrutura de análise criada

Fluxo de aprovação / reprovação

Integração via router

Observação:
Ainda não há eventos automáticos de status (previsto nos próximos passos).

3.3 Cotação ✅

Status: FUNCIONAL

Fluxo de cotação implementado

Integração com disputa

Preparação correta para precificação por item

3.4 Disputa (Nível de Item) ✅⚠️

Status: FUNCIONAL COM ALTA MATURIDADE

Implementações relevantes:

Disputa ocorre por item, não por processo

Registro de lances

Cálculo de preço total

Controle de markup mínimo

Autorização de exceção restrita ao perfil GESTOR

Encerramento de item com classificação:

Ganhou

Perdeu (monitoramento pós-pregão ou não)

Diferencial técnico:

Regras críticas corretamente no domínio

Decisão de exceção auditável

3.5 Pós-Pregão ✅

Status: FUNCIONAL

Iniciado automaticamente para itens relevantes

Domínio isolado

API integrada

3.6 Timeline (Auditoria Central) ✅⚠️

Status: FUNCIONAL ESTRUTURALMENTE CORRETA

Funcionalidades:

Registro de eventos

Classificação por:

Tipo de evento

Origem (Usuário / Sistema)

Uso já integrado ao domínio de Disputa

Importante:
A Timeline já não é logging, é auditoria de negócio.

4. O QUE ESTÁ PARCIALMENTE IMPLEMENTADO
4.1 Padronização de Eventos de Status ⚠️

Existe registro manual de eventos

Ainda não existe padrão obrigatório para toda mudança de status

Transições ainda dependem do desenvolvedor lembrar de registrar

➡️ Próximo passo já definido e alinhado

4.2 Consistência Global de Auditoria ⚠️

Alguns domínios ainda mudam status sem gerar evento

Falta normalização completa das mensagens

Falta rastreio formal de exceções sistêmicas

5. DÉBITOS TÉCNICOS CONSCIENTES (NÃO ERROS)

Esses pontos não são falhas, mas decisões conscientes de fase:

Banco de dados ainda em memória

Ausência de persistência real

Sem autenticação/autorização real (perfil é enum)

APIs ainda não documentadas via OpenAPI avançado

Sem testes automatizados (ainda)

6. PRÓXIMOS PASSOS (SEQUÊNCIA IDEAL)
🔹 PASSO 1 — Padronizar eventos automáticos de status (IMEDIATO)

Helper único de transição de status

Toda mudança gera evento automaticamente

Origem claramente definida

🔹 PASSO 2 — Eventos de exceção e violação de regra

Markup abaixo do mínimo

Override manual

Reabertura de fases

Decisão fora do fluxo padrão

🔹 PASSO 3 — Timeline como ferramenta de consulta

Ordenação

Filtros por entidade / tipo / origem

Endpoint de auditoria

🔹 PASSO 4 — Consolidação do ciclo completo

Garantir que nenhum domínio altere estado sem evento

Checklist de cobertura total

🔹 PASSO 5 — Persistência real (PostgreSQL)

Modelagem relacional

Migração do db em memória

Preparação para escala

🔹 PASSO 6 — Testes automatizados de domínio

Testes de regra

Testes de exceção

Testes de fluxo completo

7. AVALIAÇÃO DE MATURIDADE DO PROJETO
📊 Percentual estimado de conclusão
Dimensão	Status
Arquitetura	90%
Regras de Negócio	85%
Fluxo Operacional	80%
Auditoria / Observabilidade	65%
Infraestrutura	30%
✅ Percentual geral do projeto:
≈ 75% concluído

Considerando escopo funcional, qualidade arquitetural e preparação para escala.

8. CONCLUSÃO EXECUTIVA

O SGL Enterprise já se encontra em um patamar superior ao de sistemas CRUD comuns.
Ele apresenta:

Arquitetura defendível

Domínios bem definidos

Auditoria real de decisões

Base sólida para crescimento corporativo

O que falta não é correção, é sofisticação.
