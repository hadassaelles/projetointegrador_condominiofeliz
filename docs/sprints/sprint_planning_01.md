# Sprint Planning - Sprint 01

**Data:** 2026-10-15  
**Participantes:** Hadassa (PO/Dev), Antigravity (ScrumAIDev Agent)  
**Sprint Duration:** 2 semanas  
**Sprint Goal:** Estabilizar a execução do backend Django e consolidar o fluxo ponta a ponta de autenticação por perfis, navegação unificada e agendamento/consulta de reservas de áreas comuns.  
**GitHub Project:** -  
**GitHub Sprint Iteration:** -  
**GitHub Sprint Milestone:** -  

---

## Sprint Capacity

- **Velocity anterior:** N/A (Primeira Sprint)
- **Capacidade estimada:** 18 story points
- **Dias úteis disponíveis:** 10 dias
- **Impedimentos conhecidos:** Worktree local com deleções de amostras antigas pendentes de alinhamento; Django com erro de import em `mensagens/admin.py` a ser resolvido em BUG-001.

---

## Sprint Goal

> **Estabilizar o ambiente Django, unificar o redirecionamento e menus por perfil (Morador, Síndico, Funcionário) e entregar a funcionalidade de reservas de áreas comuns operando para morador e portaria.**

---

## User Stories Selecionadas

### [BUG-001] Estabilização de Rotas e Imports do Django

- **Prioridade:** Alta (Bloqueador)
- **GitHub Epic Issue:** -
- **GitHub US Issue:** -
- **Story Points:** 2
- **Assignee:** Dev Team
- **Nível ScrumAIDev:** 0
- **Exige Spec governada?** Não
- **Spec:** -
- **Exige Contract governado?** Não
- **Contract:** -
- **BDD:** -
- **Behavior change esperado:** YES
- **Critérios de Aceitação:**
  - [x] `python manage.py check` executa sem erros de importação ou de sintaxe.
  - [x] Alinhar o modelo `Mensagem` vs `Noticia` em `mensagens/` para que o Django Admin e apps carreguem normalmente.
  - [x] Corrigir rota vazia incompleta em `pessoas/urls.py`.

---

### [US-001] Autenticação e Redirecionamento por Perfil de Usuário

- **Prioridade:** Alta
- **GitHub Epic Issue:** [EPIC-001]
- **GitHub US Issue:** -
- **Story Points:** 3
- **Assignee:** Dev Team
- **Nível ScrumAIDev:** 0
- **Exige Spec governada?** Não
- **Spec:** -
- **Exige Contract governado?** Não
- **Contract:** -
- **BDD:** -
- **Behavior change esperado:** YES
- **Critérios de Aceitação:**
  - [x] Ao realizar login com credenciais válidas de Síndico, o usuário é redirecionado para `home_sindico`.
  - [x] Ao realizar login com credenciais válidas de Funcionário, o usuário é redirecionado para `home_funcionario`.
  - [x] Ao realizar login com credenciais válidas de Morador, o usuário é redirecionado para `home_morador`.
  - [x] Tentativa de acesso direto a rotas restritas por usuário sem a respectiva permissão deve bloquear ou redirecionar adequadamente.
  - [x] Botão de logout encerra a sessão e retorna à tela de login.


---

### [US-002] Conexão e Navegação Unificada nas Dashboards (Home)

- **Prioridade:** Alta
- **GitHub Epic Issue:** [EPIC-001]
- **GitHub US Issue:** -
- **Story Points:** 5
- **Assignee:** Dev Team
- **Nível ScrumAIDev:** 0
- **Exige Spec governada?** Não
- **Spec:** -
- **Exige Contract governado?** Não
- **Contract:** -
- **BDD:** -
- **Behavior change esperado:** YES
- **Critérios de Aceitação:**
  - [ ] As sidebars das telas de Morador, Síndico e Funcionário devem utilizar URLs nomeadas do Django (`{% url '...' %}`), eliminando links estáticos `.html`.
  - [ ] O nome e perfil do usuário logado devem ser exibidos dinamicamente no rodapé da barra lateral.
  - [ ] O morador consegue navegar entre Dashboard, Reservas, Ocorrências e Comunicados a partir do menu lateral.

---

### [US-003] Agendamento e Consulta de Reservas pelo Morador

- **Prioridade:** Alta
- **GitHub Epic Issue:** [EPIC-002]
- **GitHub US Issue:** -
- **Story Points:** 5
- **Assignee:** Dev Team
- **Nível ScrumAIDev:** 0
- **Exige Spec governada?** Não
- **Spec:** -
- **Exige Contract governado?** Não
- **Contract:** -
- **BDD:** -
- **Behavior change esperado:** YES
- **Critérios de Aceitação:**
  - [ ] Morador autenticado visualiza as áreas comuns disponíveis (ex: churrasqueira, salão de festas) com capacidade e ícone.
  - [ ] Morador consegue submeter formulário de nova reserva informando área, unidade, data e horário de início/término.
  - [ ] Formulário valida se os horários são coerentes (início anterior ao fim).
  - [ ] A reserva criada fica registrada e visível na listagem de reservas do morador.

---

### [US-005] Consulta de Reservas do Dia pela Portaria (Funcionário)

- **Prioridade:** Alta
- **GitHub Epic Issue:** [EPIC-002]
- **GitHub US Issue:** -
- **Story Points:** 3
- **Assignee:** Dev Team
- **Nível ScrumAIDev:** 0
- **Exige Spec governada?** Não
- **Spec:** -
- **Exige Contract governado?** Não
- **Contract:** -
- **BDD:** -
- **Behavior change esperado:** YES
- **Critérios de Aceitação:**
  - [ ] Usuário com perfil Funcionário consegue acessar a tela de Reservas do Dia.
  - [ ] A tela exibe apenas as reservas confirmadas para a data atual (`timezone.localdate()`).
  - [ ] A listagem exibe a área, morador responsável, unidade e horários de início e fim.
  - [ ] Reservas canceladas não aparecem na listagem do dia.

---

## Rastreabilidade da Sprint

- **Backlog fonte:** [docs/product_backlog.md](file:///c:/Users/hadau/Desktop/projetointegrador/projetointegrador_condominiofeliz/docs/product_backlog.md)
- **TODO técnico:** `docs/todo.md`
- **GitHub Sprint Container em uso:** -
- **Specs a criar/atualizar:** -
- **Contracts a criar/atualizar:** -
- **BDD a criar/atualizar:** -
- **Gates opcionais da sprint:** N/A (Nível ScrumAIDev 0)
- **Task Issues a criar/atualizar:** Breakdown técnico a ser gerado via `/feature-development` para cada story selecionada.

---

## Definition of Done

- [ ] Código revisado
- [ ] Decisão sobre Spec governada registrada para cada US
- [ ] Decisão sobre Contract governado registrada para cada US
- [ ] Nível ScrumAIDev registrado para cada US
- [ ] `python manage.py check` passando sem advertências ou erros
- [ ] Testes manuais do fluxo executados no navegador
- [ ] Documentação de sprint e tarefas atualizadas

---

## Riscos e Dependências

| Risco/Dependência | Impacto | Mitigação |
|---|---|---|
| Inconsistência entre classes `Mensagem` e `Noticia` no app `mensagens` | Alto | Tratar `BUG-001` como primeira tarefa prioritária da sprint antes de avançar nos fluxos de UI |
| Rotas e templates com referências a arquivos `.html` estáticos | Médio | Resolver em `US-002` padronizando com a tag `{% url %}` do Django |
| Worktree sujo com arquivos deletados em `arquivos/` | Médio | Alinhar com o usuário se os arquivos deletados devem ser removidos do controle de versão ou restaurados |

---

## Sumário de Estimativas da Sprint 01

- **BUG-001:** 2 pts
- **US-001:** 3 pts
- **US-002:** 5 pts
- **US-003:** 5 pts
- **US-005:** 3 pts
- **Total Planejado:** **18 Story Points**

