from django.urls import path
from . import views

app_name = 'encomendas'

urlpatterns = [
    path('registrar/', views.registrar_encomenda, name='registrar'),
    path('<int:encomenda_id>/retirada/', views.marcar_retirada, name='marcar_retirada'),
    path('minhas/', views.minhas_encomendas, name='minhas'),
]