import re

from django.conf import settings
from django import forms
from django.contrib.auth import get_user_model

from apartamentos.models import Apartamento

from .models import Pessoa

User = get_user_model()

# Mesmas regras do script antigo
REGEX_NOME = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$"          # só letras e espaços
REGEX_UNIDADE = r"^[A-Za-zÀ-ÖØ-öø-ÿ0-9\s\-]+$"  # letras, números, espaço e hífen


def limpar_cpf(cpf):
    """Remove pontos, traço e espaços, deixando só os dígitos."""
    return re.sub(r"\D", "", cpf or "")


def validar_cpf(cpf):
    """Valida CPF pelo algoritmo oficial dos dígitos verificadores."""
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    resto = 0 if resto == 10 else resto
    if resto != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    resto = 0 if resto == 10 else resto
    return resto == int(cpf[10])


def buscar_apartamento(numero):
    """Procura o apartamento pelo número (o model Apartamento não tem bloco)."""
    try:
        return Apartamento.objects.filter(numero=numero).first()
    except (ValueError, TypeError):
        return None


class CadastroMoradorForm(forms.Form):
    nome = forms.CharField(max_length=100)
    sobrenome = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=14)
    email = forms.EmailField()
    apartamento = forms.CharField(max_length=10)
    data_entrada = forms.DateField()

    def _so_letras(self, campo, rotulo):
        valor = self.cleaned_data[campo].strip()
        if not re.match(REGEX_NOME, valor):
            raise forms.ValidationError(f"{rotulo} não pode conter números ou símbolos.")
        return valor

    def clean_nome(self):
        return self._so_letras("nome", "O nome")

    def clean_sobrenome(self):
        return self._so_letras("sobrenome", "O sobrenome")

    def clean_cpf(self):
        cpf = limpar_cpf(self.cleaned_data["cpf"])
        if not cpf:
            raise forms.ValidationError("Informe o CPF.")
        if len(cpf) > 11:
            raise forms.ValidationError("O CPF deve ter no máximo 11 dígitos.")
        if getattr(settings, "VALIDAR_CPF", True) and not validar_cpf(cpf):
            raise forms.ValidationError("CPF inválido. Confira os números digitados.")
        if Pessoa.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Este CPF já está cadastrado!")
        return cpf

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if (
            Pessoa.objects.filter(email__iexact=email).exists()
            or User.objects.filter(username__iexact=email).exists()
        ):
            raise forms.ValidationError("Este e-mail já está cadastrado!")
        return email

    def _unidade(self, campo, rotulo):
        valor = self.cleaned_data[campo].strip()
        if not re.match(REGEX_UNIDADE, valor):
            raise forms.ValidationError(f"{rotulo} contém caracteres inválidos.")
        return valor

    def clean_apartamento(self):
        return self._unidade("apartamento", "Apartamento")

    def clean(self):
        cleaned = super().clean()
        numero = cleaned.get("apartamento")
        if numero:
            apto = buscar_apartamento(numero)
            if apto is None:
                self.add_error("apartamento", "Apartamento não encontrado.")
            else:
                cleaned["apartamento_obj"] = apto
        return cleaned