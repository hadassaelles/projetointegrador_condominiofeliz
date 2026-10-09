from django.db import models


class Reserva(models.Model):
    class Status(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        CONFIRMADA = 'CONFIRMADA', 'Confirmada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    apartamento = models.ForeignKey(
        'apartamentos.Apartamento', on_delete=models.CASCADE, related_name='reservas'
    )
    responsavel = models.ForeignKey(
        'pessoas.Morador', on_delete=models.CASCADE, related_name='reservas'
    )
    data = models.DateField()
    local = models.CharField(max_length=50)
    quant_pessoas = models.PositiveIntegerField()
    horas_ini = models.TimeField()
    horas_final = models.TimeField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDENTE)

    class Meta:
        ordering = ['-data', '-horas_ini']

    def __str__(self):
        return f"Reserva {self.local} - {self.data}"


class Convidado(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='convidados')
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome