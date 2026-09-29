from django.db import models
from django.contrib.auth.models import User

class Encomenda(models.Model):
    class Status(models.TextChoices):
        AGUARDANDO = 'AGUARDANDO', 'Aguardando retirada'
        RETIRADA = 'RETIRADA', 'Retirada'

    morador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='encomendas')
    unidade = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.AGUARDANDO)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.descricao} - {self.unidade}'