from django.db import models


class Mensagem(models.Model):
    id_mensagem = models.AutoField(primary_key=True)

    remetente = models.ForeignKey(
        'pessoas.Pessoa',
        on_delete=models.CASCADE,
        related_name='mensagens_enviadas'
    )

    destinatario = models.ForeignKey(
        'pessoas.Pessoa',
        on_delete=models.CASCADE,
        related_name='mensagens_recebidas'
    )

    tipo = models.CharField(max_length=30)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='mensagens/', null=True, blank=True)
    situacao = models.CharField(max_length=30)

    def __str__(self):
        return f'Mensagem {self.id_mensagem} - {self.remetente} → {self.destinatario}'
