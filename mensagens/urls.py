from django.urls import path
from . import views
from .models import Mensagem

app_name = 'mensagens'

urlpatterns = [
    path('mural/', views.mural, name='mural'),
    path('noticias/nova/', views.publicar_noticia, name='publicar'),
    path('noticias/<int:noticia_id>/editar/', views.editar_noticia, name='editar'),
    path('noticias/<int:noticia_id>/excluir/', views.excluir_noticia, name='excluir'),
    path('ocorrencias/nova/', views.nova_ocorrencia, name='nova_ocorrencia'),
    path('ocorrencias/', views.gerenciar_ocorrencias, name='gerenciar_ocorrencias'),
    path('sugestoes/nova/', views.nova_sugestao, name='nova_sugestao'),
    path('sugestoes/', views.gerenciar_sugestoes, name='gerenciar_sugestoes'),
    path('resolver/<int:mensagem_id>/', views.resolver_mensagem, name='resolver_mensagem'),
]