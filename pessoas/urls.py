from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('redirecionar/', views.redirecionar_apos_login, name='redirecionar_apos_login'),
    path('sindico/', views.home_sindico, name='home_sindico'),
    path('funcionario/', views.home_funcionario, name='home_funcionario'),
    path('morador/', views.home_morador, name='home_morador'),
]