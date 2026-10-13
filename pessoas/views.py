from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from .permissions import is_sindico, is_funcionario

def redirecionar_apos_login(request):
    user = request.user
    if is_sindico(user):
        return redirect('home_sindico')
    if is_funcionario(user):
        return redirect('home_funcionario')
    return redirect('home_morador')

@login_required
def home_morador(request):
    return render(request, 'pessoas/home_morador.html')

@user_passes_test(is_sindico)
def home_sindico(request):
    return render(request, 'pessoas/home_sindico.html')

@user_passes_test(is_funcionario)
def home_funcionario(request):
    return render(request, 'pessoas/home_funcionario.html')