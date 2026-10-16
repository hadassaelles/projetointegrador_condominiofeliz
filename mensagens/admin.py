from django.contrib import admin
from .models import Comunicado, Ocorrencia

@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'criado_em')
    search_fields = ('titulo', 'conteudo')

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('id_ocorrencia', 'titulo', 'categoria', 'morador', 'status', 'criado_em')
    list_filter = ('categoria', 'status', 'criado_em')
    search_fields = ('titulo', 'descricao', 'unidade')