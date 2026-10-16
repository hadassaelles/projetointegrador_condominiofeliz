# Product Backlog

**Produto:** Condomínio Feliz (Sistema de Gestão Condominial)  
**Product Owner:** Hadassa / Equipe de Projeto  
**Última atualização:** 2026-10-15  

---

## Visão do Produto

> O **Condomínio Feliz** é uma plataforma web integrada voltada à gestão operacional e convivência comunitária em condomínios residenciais. O sistema conecta moradores, síndicos e funcionários/porteiros, centralizando a reserva de áreas comuns, controle de encomendas, abertura de ocorrências e publicação de comunicados oficiais com segurança e facilidade de acesso.

---

## Backlog Items

### Alta Prioridade

#### [EPIC-001] Autenticação, Perfis e Acesso Integrado

**Objetivo:** Prover autenticação segura e navegação customizada por perfil (Morador, Síndico, Funcionário/Porteiro).  
**Valor de negócio:** Alto  
**Estimativa:** 8 pontos  
**GitHub Epic Issue:** -  

##### User Stories

| ID | Issue | Título | Story Points | Status | Sprint | Spec | Contract | BDD |
|----|-------|--------|--------------|--------|--------|------|----------|-----|
| US-001 | - | Autenticação e Redirecionamento por Perfil de Usuário | 3 | Done | Sprint 01 | - | - | - |
| US-002 | - | Conexão e Navegação Unificada nas Dashboards (Home) | 5 | Ready | Sprint 01 | - | - | - |


---

#### [EPIC-002] Gestão de Reservas de Áreas Comuns

**Objetivo:** Permitir que moradores reservem espaços compartilhados (salão de festas, churrasqueira, etc.) e que a administração e portaria acompanhem o uso.  
**Valor de negócio:** Alto  
**Estimativa:** 13 pontos  
**GitHub Epic Issue:** -  

##### User Stories

| ID | Issue | Título | Story Points | Status | Sprint | Spec | Contract | BDD |
|----|-------|--------|--------------|--------|--------|------|----------|-----|
| US-003 | - | Agendamento e Consulta de Reservas pelo Morador | 5 | Ready | Sprint 01 | - | - | - |
| US-004 | - | Gestão e Cancelamento de Reservas pelo Síndico | 3 | Backlog | Sprint 02 | - | - | - |
| US-005 | - | Consulta de Reservas do Dia pela Portaria (Funcionário) | 3 | Ready | Sprint 01 | - | - | - |
| US-006 | - | Cadastro de Convidados Vinculados à Reserva | 2 | Backlog | Sprint 02 | - | - | - |

---

### Média Prioridade

#### [EPIC-003] Controle e Notificação de Encomendas

**Objetivo:** Organizar a recepção, armazenamento e retirada de pacotes e correspondências na portaria.  
**Valor de negócio:** Médio  
**Estimativa:** 8 pontos  
**GitHub Epic Issue:** -  

##### User Stories

| ID | Issue | Título | Story Points | Status | Sprint | Spec | Contract | BDD |
|----|-------|--------|--------------|--------|--------|------|----------|-----|
| US-007 | - | Registro de Chegada e Baixa de Encomendas pela Portaria | 5 | Backlog | Sprint 02 | - | - | - |
| US-008 | - | Acompanhamento e Notificação de Encomendas pelo Morador | 3 | Backlog | Sprint 02 | - | - | - |

---

#### [EPIC-004] Comunicação, Ocorrências e Mural de Avisos

**Objetivo:** Facilitar a comunicação direta entre condôminos e a administração através de chamados/ocorrências e comunicados oficiais.  
**Valor de negócio:** Médio  
**Estimativa:** 11 pontos  
**GitHub Epic Issue:** -  

##### User Stories

| ID | Issue | Título | Story Points | Status | Sprint | Spec | Contract | BDD |
|----|-------|--------|--------------|--------|--------|------|----------|-----|
| US-009 | - | Abertura e Histórico de Ocorrências pelo Morador | 5 | Backlog | Sprint 02 | - | - | - |
| US-010 | - | Gestão e Resposta de Ocorrências pelo Síndico | 3 | Backlog | Sprint 03 | - | - | - |
| US-011 | - | Publicação e Visualização de Comunicados no Mural | 3 | Backlog | Sprint 03 | - | - | - |

---

### Baixa Prioridade

#### [EPIC-005] Gestão Cadastral de Apartamentos e Moradores

**Objetivo:** Gerenciar as unidades, moradores e vínculos de proprietários/síndico no condomínio.  
**Valor de negócio:** Baixo (suportado inicialmente via Django Admin)  
**Estimativa:** 5 pontos  
**GitHub Epic Issue:** -  

##### User Stories

| ID | Issue | Título | Story Points | Status | Sprint | Spec | Contract | BDD |
|----|-------|--------|--------------|--------|--------|------|----------|-----|
| US-012 | - | Interface Administrativa para Vínculo de Apartamentos e Moradores | 5 | Backlog | Sprint 03 | - | - | - |

---

## Technical Debt & Bugs

| ID | Descrição | Prioridade | Estimativa | Impacto |
|----|-----------|------------|------------|---------|
| BUG-001 | Correção de import de `Noticia` vs `Mensagem` e ajuste de rota em `pessoas/urls.py` | Alta | 2 | Bloqueia `manage.py check` e inicialização limpa do Django |
| DEBT-001 | Padronização dos templates base e eliminação de links estáticos `.html` nas barras de navegação | Média | 3 | Garante navegação consistente e reaproveitamento de layout |

---

## Roadmap Overview

### Sprint 01
- Estabilização da base Django (BUG-001)
- Fluxos centrais de login e dashboards por perfil (US-001, US-002)
- Módulo de reservas para Morador e Portaria (US-003, US-005)

### Sprint 02
- Aprovação/Cancelamento de reservas e lista de convidados (US-004, US-006)
- Controle de encomendas na portaria e consulta pelo morador (US-007, US-008)
- Abertura de ocorrências (US-009)

### Sprint 03
- Gestão de ocorrências e mural de avisos oficiais (US-010, US-011)
- Refinamentos cadastrais e testes end-to-end (US-012)

