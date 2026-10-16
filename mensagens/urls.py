from django.urls import path
from . import views

app_name = 'mensagens'

urlpatterns = [
    # Mural de Comunicados
    path('mural/', views.mural, name='mural'),
    path('comunicados/novo/', views.publicar_noticia, name='publicar'),
    path('comunicados/<int:noticia_id>/editar/', views.editar_noticia, name='editar'),
    path('comunicados/<int:noticia_id>/excluir/', views.excluir_noticia, name='excluir'),
    path('noticias/nova/', views.publicar_noticia, name='publicar_noticia'),

    # Fluxo de Ocorrências (Morador)
    path('ocorrencias/', views.minhas_ocorrencias, name='minhas_ocorrencias'),
    path('ocorrencias/nova/', views.nova_ocorrencia, name='nova_ocorrencia'),

    # Gestão de Ocorrências (Síndico)
    path('ocorrencias/gerenciar/', views.gerenciar_ocorrencias, name='gerenciar_ocorrencias'),
    path('ocorrencias/<int:ocorrencia_id>/status/', views.atualizar_status_ocorrencia, name='atualizar_status_ocorrencia'),
]