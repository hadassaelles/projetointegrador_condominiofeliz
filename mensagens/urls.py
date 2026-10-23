from django.urls import path
from . import views

app_name = 'mensagens'

urlpatterns = [
    path('mural/', views.mural, name='mural'),
    path('comunicados/', views.gerenciar_comunicados, name='gerenciar_comunicados'),
    path('noticias/<int:noticia_id>/editar/', views.editar_noticia, name='editar'),
    path('noticias/<int:noticia_id>/excluir/', views.excluir_noticia, name='excluir'),
    path('minhas-ocorrencias/', views.minhas_ocorrencias, name='minhas_ocorrencias'),
    path('ocorrencias/', views.gerenciar_ocorrencias, name='gerenciar_ocorrencias'),
    path('atualizar/<int:mensagem_id>/', views.atualizar_mensagem, name='atualizar_mensagem'),
]