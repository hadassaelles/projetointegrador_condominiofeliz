from django.db import models
from django.utils import timezone


class Encomenda(models.Model):
    funcionario = models.ForeignKey(
        'pessoas.Funcionario', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='encomendas_recebidas'
    )
    morador = models.ForeignKey(
        'pessoas.Morador', on_delete=models.CASCADE,
        null=True, blank=True, related_name='encomendas'
    )
    apartamento = models.ForeignKey(
        'apartamentos.Apartamento', on_delete=models.CASCADE, related_name='encomendas'
    )
    descricao = models.CharField(max_length=200, default='')
    codigo_retirada = models.CharField(max_length=20, unique=True, null=True, blank=True, editable=False)
    recebido_em = models.DateTimeField(default=timezone.now)
    entregue_em = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-recebido_em']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.codigo_retirada:
            self.codigo_retirada = f'RET-{self.pk:04d}'
            super().save(update_fields=['codigo_retirada'])

    def __str__(self):
        return f'{self.descricao} - Apto {self.apartamento.numero}'