from django.db import models


class Encomenda(models.Model):
    funcionario = models.ForeignKey(
        'pessoas.Funcionario',
        on_delete=models.SET_NULL,
        null=True,
        related_name='encomendas_recebidas',
    )
    apartamento = models.ForeignKey(
        'apartamentos.Apartamento', on_delete=models.CASCADE, related_name='encomendas'
    )

    def __str__(self):
        return f"Encomenda - Apto {self.apartamento}"