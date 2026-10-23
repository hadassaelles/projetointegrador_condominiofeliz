from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
    class Categoria(models.TextChoices):
        GERAL = 'GERAL', 'Geral'
        MANUTENCAO = 'MANUTENCAO', 'Manutenção'
        REUNIAO = 'REUNIAO', 'Reunião'
        SERVICOS = 'SERVICOS', 'Serviços'
        SEGURANCA = 'SEGURANCA', 'Segurança'

    class Prioridade(models.TextChoices):
        NORMAL = 'NORMAL', 'Normal'
        IMPORTANTE = 'IMPORTANTE', 'Importante'
        URGENTE = 'URGENTE', 'Urgente'

    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    categoria = models.CharField(max_length=20, choices=Categoria.choices, default=Categoria.GERAL)
    prioridade = models.CharField(max_length=12, choices=Prioridade.choices, default=Prioridade.NORMAL)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']
    @property
    def autor_nome(self):
        pessoa = getattr(self.autor, 'pessoa', None)
        return str(pessoa) if pessoa else (self.autor.get_full_name() or self.autor.username)

    def __str__(self):
        return self.titulo

class Mensagem(models.Model):
    class Tipo(models.TextChoices):
        MANUTENCAO = 'MANUTENCAO', 'Manutenção'
        RECLAMACAO = 'RECLAMACAO', 'Reclamação'
        SUGESTAO = 'SUGESTAO', 'Sugestão'
        DENUNCIA = 'DENUNCIA', 'Denúncia'

    class Situacao(models.TextChoices):
        ABERTA = 'ABERTA', 'Aberta'
        EM_ANDAMENTO = 'EM_ANDAMENTO', 'Em andamento'
        RESOLVIDA = 'RESOLVIDA', 'Resolvida'

    id_mensagem = models.AutoField(primary_key=True)
    remetente = models.ForeignKey('pessoas.Pessoa', on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey('pessoas.Pessoa', on_delete=models.CASCADE, null=True, blank=True, related_name='mensagens_recebidas')
    responsavel = models.ForeignKey('pessoas.Funcionario', on_delete=models.SET_NULL, null=True, blank=True, related_name='ocorrencias_atribuidas')
    titulo = models.CharField(max_length=150, default='')
    tipo = models.CharField(max_length=30, choices=Tipo.choices)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='mensagens/', null=True, blank=True)
    situacao = models.CharField(max_length=30, choices=Situacao.choices, default=Situacao.ABERTA)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f'Mensagem {self.id_mensagem} - {self.remetente} → {self.destinatario}'