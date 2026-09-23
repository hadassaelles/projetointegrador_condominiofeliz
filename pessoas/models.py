from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Telefone(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='telefones')
    tipo = models.CharField(max_length=20)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.numero} ({self.pessoa})"


class Morador(Pessoa):
    apartamento = models.ForeignKey(
        'apartamentos.Apartamento',
        on_delete=models.CASCADE,
        related_name='moradores',
    )

    def __str__(self):
        return f"{self.nome} (Morador - Apto {self.apartamento_id})"


class Sindico(Pessoa):
    def __str__(self):
        return f"{self.nome} (Sindico)"


class Funcionario(Pessoa):
    cargo = models.CharField(max_length=100)
    sindico = models.ForeignKey(
        Sindico,
        on_delete=models.SET_NULL,
        null=True,
        related_name='funcionarios',
    )

    def __str__(self):
        return f"{self.nome} ({self.cargo})"
