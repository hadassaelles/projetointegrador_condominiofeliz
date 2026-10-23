from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from .permissions import is_sindico, is_funcionario, get_funcionario, get_morador
from datetime import timedelta
from django.utils import timezone
from encomendas.models import Encomenda
from reservas.models import Reserva
from mensagens.models import Noticia, Mensagem

def redirecionar_apos_login(request):
    user = request.user
    if is_sindico(user):
        return redirect('home_sindico')
    if is_funcionario(user):
        return redirect('home_funcionario')
    return redirect('home_morador')

@login_required
def home_morador(request):
    hoje = timezone.localdate()
    pessoa = getattr(request.user, 'pessoa', None)
    morador = get_morador(request.user)

    if morador:
        ocorrencias = Mensagem.objects.filter(remetente_id=morador.pk)
        reservas = (
            Reserva.objects.filter(responsavel=morador, data__gte=hoje)
            .exclude(status=Reserva.Status.CANCELADA)
            .order_by('data', 'horas_ini')
        )
        unidade = morador.apartamento.numero
    else:
        ocorrencias = Mensagem.objects.none()
        reservas = Reserva.objects.none()
        unidade = None

    sete_dias = timezone.now() - timedelta(days=7)

    return render(request, 'pessoas/home_morador.html', {
        'nome': pessoa.nome if pessoa else request.user.username,
        'unidade': unidade,
        'qtd_abertas': ocorrencias.filter(situacao=Mensagem.Situacao.ABERTA).count(),
        'ocorrencias_recentes': ocorrencias[:5],
        'qtd_reservas': reservas.count(),
        'proxima_reserva': reservas.first(),
        'novos_comunicados': Noticia.objects.filter(criado_em__gte=sete_dias).count(),
    })

@user_passes_test(is_sindico)
def home_sindico(request):
    return render(request, 'pessoas/home_sindico.html')

@user_passes_test(is_funcionario)
def home_funcionario(request):
    hoje = timezone.localdate()
    pessoa = getattr(request.user, 'pessoa', None)
    funcionario = get_funcionario(request.user)

    pendentes = Encomenda.objects.filter(entregue_em__isnull=True).select_related('morador', 'apartamento')
    reservas_futuras = (
        Reserva.objects.filter(data__gte=hoje)
        .exclude(status=Reserva.Status.CANCELADA)
        .order_by('data', 'horas_ini')
    )
    sete_dias = timezone.now() - timedelta(days=7)

    return render(request, 'pessoas/home_funcionario.html', {
        'nome': pessoa.nome if pessoa else request.user.username,
        'nome_completo': str(pessoa) if pessoa else request.user.username,
        'cargo': funcionario.cargo if funcionario else 'Funcionário',
        'qtd_pendentes': pendentes.count(),
        'encomendas_recentes': pendentes[:5],
        'qtd_reservas': reservas_futuras.count(),
        'proxima_reserva': reservas_futuras.first(),
        'novos_comunicados': Noticia.objects.filter(criado_em__gte=sete_dias).count(),
    })