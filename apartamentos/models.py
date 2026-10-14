from django.db import models

class Apartamento(models.Model):
    numero = models.CharField(max_length=10)
    proprietario = models.ForeignKey(
        'pessoas.Morador',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='apartamentos_proprios',
    )
    sindico = models.ForeignKey(
        'pessoas.Sindico',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='apartamentos_administrados',
    )

    def __str__(self):
        return f"Apto {self.numero}"
