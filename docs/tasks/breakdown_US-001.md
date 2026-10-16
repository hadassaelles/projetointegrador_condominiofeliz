# Task Breakdown: [US-001] Autenticação e Redirecionamento por Perfil de Usuário

**Data:** 2026-10-15  
**Participantes:** Hadassa, Antigravity  
**Estimativa total:** 3 Story Points  
**Nível ScrumAIDev:** 0  
**Spec governada:** N/A  
**Contract governado:** N/A  
**Padrão de erro:** N/A  
**BDD associado:** N/A  
**Behavior change:** YES  
**GitHub Epic Issue:** [EPIC-001]  
**GitHub Parent US Issue:** -  
**GitHub Sprint Container:** Sprint 01  

---

## Pré-Flight de Governança

- **US exige Spec governada?** Não (Nível 0, regras nativas de autenticação Django).
- **US exige Contract governado?** Não.
- **Justificativa do Nível ScrumAIDev:** Nível 0 é suficiente pois utiliza as views e middlewares nativos de autenticação e sessão do Django (`django.contrib.auth`).
- **Touch List aplicável:**
  - `pessoas/permissions.py`
  - `pessoas/views.py`
  - `pessoas/urls.py`
  - `condominiofeliz/settings.py`

---

## Tasks Técnicas

### Backend Tasks

#### [TASK-001] Refinamento de Permissões por Perfil
- **Descrição:** Atualizar `pessoas/permissions.py` com detecção robusta de perfis (`is_sindico`, `is_funcionario`, `is_morador`), verificando superusuário, grupos Django e relacionamentos de models (`hasattr(user, 'pessoa')`).
- **Status:** Done
- **Dependências:** Nenhuma

#### [TASK-002] Fluxo de Redirecionamento após Login
- **Descrição:** Validar e garantir que `redirecionar_apos_login` direcione Síndico para `home_sindico`, Funcionário para `home_funcionario` e Morador para `home_morador`.
- **Status:** Done
- **Dependências:** TASK-001

#### [TASK-003] Encerramento Seguro de Sessão (Logout)
- **Descrição:** Garantir compatibilidade de logout com formulário POST e redirecionamento para `LOGIN_URL`.
- **Status:** Done
- **Dependências:** Nenhuma

