### Instalação Oficial

Analise integralmente este projeto Django e prepare-o para que qualquer desenvolvedor consiga executá-lo em um ambiente Windows limpo possuindo apenas:

   ```
   Python instalado
   Git instalado
   ```

O objetivo é que, após clonar o repositório, seja possível instalar automaticamente o Django e todas as dependências necessárias sem necessidade de descobrir bibliotecas faltantes ou realizar configurações não documentadas.

## Fase 1 - Análise Completa do Projeto

Realize uma análise completa do código-fonte.

Identifique:
```
Versão mínima do Python necessária
Versão do Django utilizada
Apps Django instalados
Bibliotecas Python utilizadas
Dependências indiretas
Banco de dados utilizado
Serviços externos utilizados
Variáveis de ambiente obrigatórias
Arquivos ausentes para execução
Dependências do sistema operacional necessárias
```

Analise especialmente:

```
Python
INSTALLED_APPS
Python
MIDDLEWARE
Python
DATABASES
Python
settings.py
Python
settings/*.py
Python
requirements.txt
Python
pyproject.toml
```

Verifique todos os imports do projeto e extraia as dependências reais utilizadas.

## Fase 2 - Dependências Python

Crie ou atualize:

```
Plain Text
requirements.txt
```

O arquivo deve conter obrigatoriamente:

- Plain Text
- Django


### Regras:

Não inventar dependências.
Identificar dependências através dos imports encontrados.
Garantir compatibilidade entre versões.
Atualizar o arquivo com as dependências efetivamente utilizadas.

Caso necessário, gerar:

```
PowerShell
pip freeze > requirements.txt
```
## Fase 3 - Ambiente Virtual

Documentar no README o processo de criação do ambiente virtual.

**Criar ambiente:**

```
PowerShell
python -m venv venv
```

**Ativar ambiente:**

```
PowerShell
venv\Scripts\activate
```
**Confirmar ativação:**

```
PowerShell
where python
```

## Fase 4 - Instalação Automática do Django

Garantir que o README deixe explícito que o Django será instalado automaticamente através de:

```
PowerShell
pip install -r requirements.txt
```

O usuário não deverá precisar executar:

```
PowerShell
pip install django
```
manualmente.

O Django deve estar listado dentro do:

```
Plain Text
requirements.txt
```
junto com todas as demais dependências.

Instalação Manual do Django (Opcional)

**Caso o usuário deseje instalar apenas o Django manualmente:**

```
PowerShell
pip install django
```
**Verificar instalação:**
```
PowerShell
django-admin --version
```
**ou**

```
PowerShell
python -m django --version
```
## Fase 5 - Variáveis de Ambiente

Criar:
```
Plain Text
.env.example
```
Contendo todas as variáveis exigidas pelo projeto.

Exemplo:

Plain Text
env não tem suporte total. O realce de sintaxe é baseado em Plain Text.
```
SECRET_KEY=
 
DEBUG=True
 
ALLOWED_HOSTS=
 
DATABASE_URL=
 
EMAIL_HOST=
 
EMAIL_PORT=
 
EMAIL_HOST_USER=
 
EMAIL_HOST_PASSWORD=
```
**Regras:**

Nunca incluir senhas reais.
Nunca incluir chaves privadas.
Nunca incluir credenciais de produção.

## Fase 6 - Configuração do Banco de Dados

Identificar qual banco está sendo utilizado.
```
SQLite
```
Documentar:
```
Plain Text
```
Nenhuma instalação adicional necessária.
```
PostgreSQL
```
Documentar a instalação para Windows.

Incluir instruções para:
```
Download
Instalação
Criação do banco
Configuração da variável DATABASE_URL
MySQL
```
Documentar:
```
Download
Instalação
Configuração
Driver Python necessário
```
Verificar configurações em:
```
Python
DATABASES
```
## Fase 7 - Migrações

Garantir que o README contenha:
```
PowerShell
python manage.py makemigrations
 
python manage.py migrate
```
Verificar:
```
Migrations quebradas
Conflitos de migrations
Dependências ausentes
```
Corrigir inconsistências encontradas.

## Fase 8 - Arquivo .gitignore

Criar ou atualizar:

```
Plain Text
.gitignore
```
Conteúdo mínimo:

```
.ignore
```

### Ambiente virtual

```
venv/
.env
 ```

### Python

```
__pycache__/
*.pyc
*.pyo
*.pyd
 ```

### Banco local

```
db.sqlite3
 ```

### Arquivos de mídia

```
media/
 ```

### Arquivos estáticos

```
staticfiles/
 ```

### VS Code

```
.vscode/
 ```

### JetBrains

```
.idea/
 ```

### Sistema

```
Thumbs.db
 ```

### Logs

```
*.log
```

## Fase 9 - Estrutura Recomendada

Garantir a seguinte estrutura:

```
Plain Text
project/
│
├── apps/
├── core/
├── docs/
├── tests/
├── templates/
├── static/
├── media/
├── scripts/
│
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── manage.py
 

## Fase 10 - Script Automático Windows

Criar:

```
Plain Text
scripts/setup.ps1
```

O script deve:

```
Criar ambiente virtual
Ativar ambiente virtual
Instalar dependências
Criar .env a partir do .env.example
Aplicar migrations
Executar validações do Django
```

Fluxo esperado:

```
PowerShell
Set-ExecutionPolicy -Scope Process Bypass
 
.\scripts\setup.ps1
```

## Fase 11 - README Completo

Gerar ou atualizar o README contendo:

```
Requisitos
Plain Text
Python 3.x
Git
Clonando o projeto
PowerShell
git clone <repositorio>
``` 

cd <repositorio>
Criando ambiente virtual

```
PowerShell
python -m venv venv
Ativando ambiente virtual
PowerShell
venv\Scripts\activate
Instalando dependências
PowerShell
pip install -r requirements.txt
Configurando variáveis de ambiente
PowerShell
copy .env.example .env
Executando migrações
PowerShell
python manage.py migrate
Criando administrador
PowerShell
python manage.py createsuperuser
``` 

Executando servidor

```
PowerShell
python manage.py runserver
Acessando o sistema
Plain Text
http://127.0.0.1:8000
Painel administrativo
Plain Text
http://127.0.0.1:8000/admin
```

## Fase 12 - Validação Final

Executar:

```
PowerShell
python manage.py check
```

Executar:

```
PowerShell
python manage.py makemigrations
```

Executar:

```
PowerShell
python manage.py migrate
```

Executar:

```
PowerShell
python manage.py runserver
```

Verificar:

```
✅ Django instalado corretamente
✅ Todas as dependências instaladas
✅ Banco configurado
✅ Variáveis de ambiente documentadas
✅ Admin funcionando
✅ Projeto inicia sem erros
✅ requirements.txt atualizado
✅ README atualizado
✅ Script setup.ps1 criado
✅ Projeto pronto para GitHub
```
Critério de Sucesso Obrigatório

**Uma pessoa em um computador Windows limpo deve conseguir executar apenas:**
```
PowerShell
git clone <repositorio>
 ```
cd <repositorio>
 ```
python -m venv venv

venv\Scripts\activate
 
pip install -r requirements.txt
 
copy .env.example .env
 
python manage.py migrate
 
python manage.py runserver
```
Sem precisar instalar Django manualmente, sem precisar descobrir dependências faltantes e sem precisar realizar configurações extras que não estejam documentadas no repositório.
