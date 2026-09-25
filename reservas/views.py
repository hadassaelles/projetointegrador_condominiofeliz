from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from pessoas.permissions import is_sindico, is_funcionario
from .models import Area, Reserva
from .forms import ReservaForm


@login_required
def dashboard_morador(request):
    context = {
        'areas': Area.objects.all(),
        'reservas': Reserva.objects.select_related('area', 'morador').all(),
    }
    return render(request, 'reservas/reservas_morador.html', context)


@login_required
def nova_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.morador = request.user
            reserva.status = Reserva.Status.CONFIRMADA
            reserva.save()
            return redirect('reservas:dashboard_morador')
    else:
        form = ReservaForm()
    return render(request, 'reservas/nova_reserva.html', {'form': form})


@user_passes_test(is_sindico)
def gerenciar_reservas(request):
    reservas = Reserva.objects.select_related('area', 'morador').all()
    return render(request, 'reservas/gerenciar_reservas.html', {'reservas': reservas})


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
    ).select_related('area', 'morador')
    return render(request, 'reservas/reservas_dia.html', {'reservas': reservas, 'hoje': hoje})