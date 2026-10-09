from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from pessoas.permissions import is_sindico, is_funcionario, get_morador
from .models import Reserva
from .forms import ReservaForm


@login_required
def dashboard_morador(request):
    context = {
        'reservas': Reserva.objects.select_related('apartamento', 'responsavel').all(),
    }
    return render(request, 'reservas/reservas_morador.html', context)


@login_required
def nova_reserva(request):
    morador = get_morador(request.user)
    if morador is None:
        return redirect('reservas:dashboard_morador')

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.responsavel = morador
            reserva.apartamento = morador.apartamento
            reserva.status = Reserva.Status.PENDENTE
            reserva.save()
            return redirect('reservas:dashboard_morador')
    else:
        form = ReservaForm()
    return render(request, 'reservas/nova_reserva.html', {'form': form})


@user_passes_test(is_sindico)
def gerenciar_reservas(request):
    reservas = Reserva.objects.select_related('apartamento', 'responsavel').all()
    return render(request, 'reservas/gerenciar_reservas.html', {'reservas': reservas})


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
    reservas = Reserva.objects.filter(data=hoje).exclude(
        status=Reserva.Status.CANCELADA
    ).select_related('apartamento', 'responsavel')
    return render(request, 'reservas/reservas_dia.html', {'reservas': reservas, 'hoje': hoje})