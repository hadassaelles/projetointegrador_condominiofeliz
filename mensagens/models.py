from django.db import models
class Mensagem(models.Model):
    id_mensagem = models.AutoField(primary_key=True)

    remetente = models.ForeignKey(
        'pessoas.Pessoa',
        on_delete=models.CASCADE,
        related_name='mensagens_enviadas',
    )

    destinatario = models.ForeignKey(
        'pessoas.Pessoa',
        on_delete=models.CASCADE,
        related_name='mensagens_recebidas',
        null=True,
        blank=True,
    )

    titulo = models.CharField(max_length=150, blank=True)
    tipo = models.CharField(max_length=30)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='mensagens/', null=True, blank=True)
    situacao = models.CharField(max_length=30, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.remetente} -> {self.destinatario or 'Todos'}"
