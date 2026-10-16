# Instalação

## Requisitos
**Antes de começar, certifique-se de ter instalado:**

```
- Python 3.x
- Git
```

Verificando as instalações
Verifique se o **Python** está instalado:

```
python --version
```
Verifique se o **Git** está instalado:

```
git --version
```

**Clonando o projeto**
```
git clone <repositorio>

cd <repositorio>
```

**Criando ambiente virtual**
```
python -m venv venv
```

**Ativando ambiente virtual**
```
venv\Scripts\activate
```

**Instalando Django e dependências**
O Django e todas as bibliotecas necessárias serão instalados automaticamente através do arquivo requirements.txt.
```
pip install -r requirements.txt
```
**Verificando a instalação do Django**
```
django-admin --version
```

ou
```
python -m django --version
```

**Configurando variáveis de ambiente**
```
copy .env.example .env
```

**Aplicando migrações**

```
python manage.py migrate
```

**Executando o projeto**
```
python manage.py runserver
```

**Acessando o sistema**
```
http://127.0.0.1:8000
```
**Painel administrativo**
```
http://127.0.0.1:8000/admin
```

**Instalação Manual do Django (Opcional)**
Caso deseje instalar apenas o Django **manualmente**:

```
pip install django
```

Verifique:

```
django-admin --version
```

Critério de Sucesso
Uma pessoa em um computador novo deve conseguir executar apenas:

```
git clone <repositorio>

cd <repositorio>

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

copy .env.example .env

python manage.py migrate

python manage.py runserver
```