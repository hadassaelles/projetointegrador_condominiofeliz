from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .permissions import is_sindico
from django.shortcuts import redirect
from pessoas.permissions import is_funcionario

def redirecionar_apos_login(request):
    user = request.user
    if is_sindico(user):
        return redirect('home_sindico')
    if user.groups.filter(name='Funcionario').exists():
        return redirect('home_funcionario')
    return redirect('reservas:dashboard_morador')

@user_passes_test(is_sindico)
def home_sindico(request):
    return render(request, 'pessoas/home_sindico.html')

@user_passes_test(is_funcionario)
def home_funcionario(request):
    return render(request, 'pessoas/home_funcionario.html')