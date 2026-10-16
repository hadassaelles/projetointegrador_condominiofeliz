# Instalação

## Requisitos
**- Antes de começar, certifique-se de ter instalado:**

```
- Python 3.x
- Git
```

## Verificando as instalações

### Verifique se o **Python** está instalado:

```
python --version
```

### **Caso o Python não esteja instalado**
Baixe e instale o Python pelo site oficial:

```
https://www.python.org/downloads/
```

Durante a instalação, marque a opção:

```
Add Python to PATH
```

Após instalar, verifique:

```
python --version
```

Resultado esperado:
```
Python 3.x.x
```


### Verifique se o **Git** está instalado:

```
git --version
```

### **Caso o Git não esteja instalado**

Baixe e instale o Git pelo site oficial:

```
https://git-scm.com/download/win
```

Após instalar, verifique:
```
git --version
```
Resultado esperado:
```
git version x.x.x
```

## **Clonando o projeto**
```
git clone https://github.com/hadassaelles/projetointegrador_condominiofeliz.git

cd projetointegrador_condominiofeliz
```

## **Criando ambiente virtual**
```
python -m venv venv
```

## **Ativando ambiente virtual**
```
venv\Scripts\activate
```

## **Instalando Django e dependências**
- O Django e todas as bibliotecas necessárias serão instalados automaticamente através do arquivo requirements.txt.
```
pip install -r requirements.txt
```
## **Verificando a instalação do Django**
```
django-admin --version
```

ou
```
python -m django --version
```

## **Configurando variáveis de ambiente**
```
copy .env.example .env
```

## **Aplicando migrações**

```
python manage.py migrate
```

## **Executando o projeto**
```
python manage.py runserver
```

## **Acessando o sistema**
```
http://127.0.0.1:8000
```
## **Painel administrativo**
```
http://127.0.0.1:8000/admin
```

## **Instalação Manual do Django (Opcional)**
- Caso deseje instalar apenas o Django **manualmente**:

```
pip install django
```

Verifique:

```
django-admin --version
```

## 1. Instalar dependências
```
pip install -r requirements.txt
```
## 2. Criar as tabelas
```
python manage.py migrate
```
## 3. Popular com dados iniciais de teste (usuários, aptos, áreas)
```
python manage.py popular_banco
```
## 4. Iniciar o sistema
```
python manage.py runserver
```
## 5. Critério de Sucesso
- Uma pessoa em um computador novo deve conseguir executar apenas:

```
git clone https://github.com/hadassaelles/projetointegrador_condominiofeliz.git

cd projetointegrador_condominiofeliz

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

copy .env.example .env

python manage.py migrate

python manage.py runserver
```