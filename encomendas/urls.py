from django.urls import path
from . import views

app_name = 'encomendas'

urlpatterns = [
    path('registrar/', views.registrar_encomenda, name='registrar'),
    path('<int:encomenda_id>/entrega/', views.registrar_entrega, name='registrar_entrega'),
    path('minhas/', views.minhas_encomendas, name='minhas'),
]