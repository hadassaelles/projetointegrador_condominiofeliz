from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from pessoas.permissions import is_funcionario, get_funcionario, get_morador
from .models import Encomenda
from .forms import EncomendaForm


@user_passes_test(is_funcionario)
def registrar_encomenda(request):
    if request.method == 'POST':
        form = EncomendaForm(request.POST)
        if form.is_valid():
            encomenda = form.save(commit=False)
            encomenda.apartamento = encomenda.morador.apartamento
            encomenda.funcionario = get_funcionario(request.user)
            encomenda.save()
            return redirect('encomendas:registrar')
    else:
        form = EncomendaForm(initial={'recebido_em': timezone.localtime()})

    encomendas = Encomenda.objects.select_related('morador', 'apartamento')
    return render(request, 'encomendas/encomendas_funcionario.html', {
        'form': form,
        'encomendas': encomendas,
    })


@user_passes_test(is_funcionario)
def registrar_entrega(request, encomenda_id):
    encomenda = get_object_or_404(Encomenda, id=encomenda_id)
    if request.method == 'POST' and not encomenda.entregue_em:
        valor = request.POST.get('entrega')
        entrega = parse_datetime(valor) if valor else None
        if entrega:
            if timezone.is_naive(entrega):
                entrega = timezone.make_aware(entrega)
            if entrega >= encomenda.recebido_em:
                encomenda.entregue_em = entrega
                encomenda.save(update_fields=['entregue_em'])
    return redirect('encomendas:registrar')


@login_required
def minhas_encomendas(request):
    morador = get_morador(request.user)
    pessoa = getattr(request.user, 'pessoa', None)
    encomendas = (
        Encomenda.objects.filter(apartamento=morador.apartamento)
        if morador else Encomenda.objects.none()
    )
    return render(request, 'encomendas/minhas.html', {
        'encomendas': encomendas,
        'nome': pessoa.nome if pessoa else request.user.username,
    })