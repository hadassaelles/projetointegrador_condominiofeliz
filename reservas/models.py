from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
    nome = models.CharField(max_length=100)
    icone = models.CharField(max_length=10, default='📍')
    capacidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    class Status(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        CONFIRMADA = 'CONFIRMADA', 'Confirmada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='reservas')
    morador = models.ForeignKey(User, on_delete=models.CASCADE)
    unidade = models.CharField(max_length=30)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDENTE)

    class Meta:
        ordering = ['-data', '-hora_inicio']

    def __str__(self):
        return f'{self.area} - {self.data}'