from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path('minhas/', views.dashboard_morador, name='dashboard_morador'),
    path('nova/', views.nova_reserva, name='nova'),
    path('gerenciar/', views.gerenciar_reservas, name='gerenciar'),
    path('gerenciar/<int:reserva_id>/cancelar/', views.cancelar_reserva, name='cancelar'),
    path('do-dia/', views.reservas_do_dia, name='do_dia'),
]