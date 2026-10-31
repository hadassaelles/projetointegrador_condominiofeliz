from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from pessoas.permissions import is_sindico, is_funcionario, get_morador
from .models import Reserva
from .forms import ReservaForm
from .areas import AREAS_COMUNS
from django.contrib import messages

@login_required
def dashboard_morador(request):
    morador = get_morador(request.user)
    hoje = timezone.localdate()

    if request.method == 'POST':
        if morador is None:
            return redirect('redirecionar_apos_login')
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.responsavel = morador
            reserva.apartamento = morador.apartamento
            reserva.status = Reserva.Status.PENDENTE
            reserva.save()
            messages.success(request, 'Reserva solicitada! Aguarde a confirmação do síndico.')
            return redirect('reservas:dashboard_morador')
    else:
        form = ReservaForm()

    reservas = (
        Reserva.objects.filter(data__gte=hoje)
        .select_related('apartamento', 'responsavel')
        .order_by('data', 'horas_ini')
    )
    return render(request, 'reservas/reservas_morador.html', {
        'form': form,
        'reservas': reservas,
        'areas': AREAS_COMUNS,
        'pode_reservar': morador is not None,
    })

@user_passes_test(is_sindico)
def gerenciar_reservas(request):
    reservas = Reserva.objects.select_related('apartamento', 'responsavel')
    return render(request, 'reservas/reservas_sindico.html', {
        'reservas': reservas,
        'areas': AREAS_COMUNS,
    })


@user_passes_test(is_sindico)
def confirmar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        reserva.status = Reserva.Status.CONFIRMADA
        reserva.save()
    return redirect('reservas:gerenciar')


@user_passes_test(is_sindico)
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        reserva.status = Reserva.Status.CANCELADA
        reserva.save()
    return redirect('reservas:gerenciar')


@user_passes_test(is_funcionario)
def reservas_do_dia(request):
    hoje = timezone.localdate()
    reservas = (
        Reserva.objects.filter(data__gte=hoje)
        .select_related('apartamento', 'responsavel')
        .order_by('data', 'horas_ini')
    )
    return render(request, 'reservas/reservas_funcionario.html', {
        'reservas': reservas,
        'areas': AREAS_COMUNS,
        'hoje': hoje,
    })