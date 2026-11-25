# TRABALHO DE PI:  Condomínio Feliz
Trabalho desenvolvido durante a disciplina de projeto Integrador

### 1. COMPONENTES<br>
Ana Beatriz Soares - anabeeas12@gmail.com <br>
Ana Clara Vianna - anaclaravianna2005@gmail.com <br>
Arthur de Oliveira Matias dos Santos - ao451427@gmail.com <br>
Hadassa Daulani Elles - hadaulles@gmail.com <br>
Isabelly Rodrigues Neves - isa.secund07@gmail.com <br>
Pietro de Oliveira Mantovani - mantovanipietro05@gmail.com <br>

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

**Windows:**

```
venv\Scripts\Activate
```

**Linux:**
```
source venv/bin/activate
```


## 4. Instalar as dependências

Com a venv ativa:

```
pip install -r requirements.txt
```
> Sempre que abrir um terminal novo para trabalhar no projeto, repita este passo.

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
