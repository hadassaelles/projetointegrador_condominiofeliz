from django.db import models
from django.contrib.auth.models import User


class Comunicado(models.Model):
    """Comunicados oficiais enviados pelo síndico para todos os moradores (Mural)."""
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunicados')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Comunicado'
        verbose_name_plural = 'Comunicados'

    def __str__(self):
        return self.titulo


# Alias para retrocompatibilidade
Noticia = Comunicado


class Ocorrencia(models.Model):
    """Ocorrências e chamados abertos pelos moradores para o síndico."""

    class Categoria(models.TextChoices):
        MANUTENCAO = 'MANUTENCAO', 'Manutenção'
        RECLAMACAO = 'RECLAMACAO', 'Reclamação'
        SUGESTAO = 'SUGESTAO', 'Sugestão'
        DENUNCIA = 'DENUNCIA', 'Denúncia'
        OUTROS = 'OUTROS', 'Outros'

    class Status(models.TextChoices):
        ABERTA = 'ABERTA', 'Aberta'
        EM_ANDAMENTO = 'EM_ANDAMENTO', 'Em andamento'
        RESOLVIDA = 'RESOLVIDA', 'Resolvida'
        CANCELADA = 'CANCELADA', 'Cancelada'

    id_ocorrencia = models.AutoField(primary_key=True)
    morador = models.ForeignKey(
        'pessoas.Pessoa',
        on_delete=models.CASCADE,
        related_name='ocorrencias_enviadas'
    )
    responsavel = models.ForeignKey(
        'pessoas.Pessoa',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ocorrencias_atribuidas'
    )
    categoria = models.CharField(
        max_length=30,
        choices=Categoria.choices,
        default=Categoria.RECLAMACAO
    )
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    unidade = models.CharField(max_length=50, blank=True)
    imagem = models.FileField(upload_to='ocorrencias/', null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ABERTA
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'

    def __str__(self):
        return f'Ocorrência #{self.id_ocorrencia} - {self.titulo} ({self.get_categoria_display()})'


# Alias para retrocompatibilidade
Mensagem = Ocorrencia