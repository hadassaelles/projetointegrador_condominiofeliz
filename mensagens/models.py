from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo

class Mensagem(models.Model):
    class Tipo(models.TextChoices):
        RECLAMACAO = 'RECLAMACAO', 'Reclamação'
        DENUNCIA = 'DENUNCIA', 'Denúncia'
        SUGESTAO = 'SUGESTAO', 'Sugestão'

    class Situacao(models.TextChoices):
        ABERTA = 'ABERTA', 'Aberta'
        RESOLVIDA = 'RESOLVIDA', 'Resolvida'

    id_mensagem = models.AutoField(primary_key=True)
    remetente = models.ForeignKey('pessoas.Pessoa', on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey('pessoas.Pessoa', on_delete=models.CASCADE, null=True, blank=True, related_name='mensagens_recebidas')
    tipo = models.CharField(max_length=30, choices=Tipo.choices)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='mensagens/', null=True, blank=True)
    situacao = models.CharField(max_length=30, choices=Situacao.choices, default=Situacao.ABERTA)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f'Mensagem {self.id_mensagem} - {self.remetente} → {self.destinatario}'