# Condomínio Feliz — Guia de Instalação

## Pré-requisitos

- **Python 3.12**
- **Git**

Confirme se os dois estão instalados:

```
python --version
git --version
```

## 1. Clonar o repositório

```
git clone https://github.com/hadassaelles/projetointegrador_condominiofeliz.git
cd projetointegrador_condominiofeliz
```

## 2. Criar o ambiente virtual (venv)

```
python -m venv venv
```

## 3. Ativar a venv

**Windows (PowerShell):**

```
venv\Scripts\Activate
```


## 4. Instalar as dependências

Com a venv ativa:

```
pip install -r requirements.txt
```
> Sempre que abrir um terminal novo para trabalhar no projeto, repita este passo.

## 5. Criar o banco de dados

```
python manage.py migrate
python manage.py popular_banco
```

Esse comando cria os usuários de teste, os apartamentos e os dados iniciais. Pode ser executado mais de uma vez sem duplicar nada.

O `db.sqlite3` não vai para o Git, então **cada máquina tem o seu próprio banco**. Por isso este passo precisa ser feito em cada computador.

## 7. Iniciar o servidor

```
python manage.py runserver
```

Abra no navegador: <http://127.0.0.1:8000/>

Para parar o servidor, pressione `Ctrl+C` no terminal.

## 8. Fazer login


| Usuário       | Perfil      | Senha           |
|---------------|-------------|-----------------|
| `sindico`     | Síndico     | `condominio123` |
| `funcionario` | Funcionário | `condominio123` |
| `morador`     | Morador     | `condominio123` |

O síndico também acessa o painel administrativo em <http://127.0.0.1:8000/admin/>.