from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from pessoas.permissions import is_funcionario
from .models import Encomenda
from .forms import EncomendaForm


@user_passes_test(is_funcionario)
def registrar_encomenda(request):
    if request.method == 'POST':
        form = EncomendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('encomendas:registrar')
    else:
        form = EncomendaForm()

    encomendas = Encomenda.objects.all()
    return render(request, 'encomendas/registrar.html', {'form': form, 'encomendas': encomendas})


@user_passes_test(is_funcionario)
def marcar_retirada(request, encomenda_id):
    encomenda = get_object_or_404(Encomenda, id=encomenda_id)
    if request.method == 'POST':
        encomenda.status = Encomenda.Status.RETIRADA
        encomenda.save()
    return redirect('encomendas:registrar')


@login_required
def minhas_encomendas(request):
    encomendas = Encomenda.objects.filter(morador=request.user)
    return render(request, 'encomendas/minhas.html', {'encomendas': encomendas})