from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .permissions import is_sindico, is_funcionario


@login_required
def redirecionar_apos_login(request):
    user = request.user
    if is_sindico(user):
        return redirect('home_sindico')
    if is_funcionario(user):
        return redirect('home_funcionario')
    return redirect('home_morador')


@user_passes_test(is_sindico)
def home_sindico(request):
    return render(request, 'pessoas/sindico/home.html', {
        'usuario': request.user,
    })


@user_passes_test(is_funcionario)
def home_funcionario(request):
    return render(request, 'pessoas/funcionario/home.html', {
        'usuario': request.user,
    })


@login_required
def home_morador(request):
    morador = getattr(getattr(request.user, 'pessoa', None), 'morador', None)
    return render(request, 'pessoas/morador/home.html', {
        'usuario': request.user,
        'morador': morador,
    })