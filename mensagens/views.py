from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from datetime import timedelta
from django.utils import timezone
from pessoas.models import Funcionario
from pessoas.permissions import is_sindico, is_funcionario, get_morador
from .models import Noticia, Mensagem
from .forms import NoticiaForm, OcorrenciaForm
from django.contrib import messages

def _estatisticas_comunicados():
    sete_dias = timezone.now() - timedelta(days=7)
    noticias = Noticia.objects.select_related('autor')
    return {
        'noticias': noticias,
        'novos_7_dias': noticias.filter(criado_em__gte=sete_dias).count(),
        'importantes': noticias.filter(
            prioridade__in=[Noticia.Prioridade.IMPORTANTE, Noticia.Prioridade.URGENTE]
        ).count(),
        'total': noticias.count(),
    }


@login_required
def mural(request):
    if is_sindico(request.user):
        return redirect('mensagens:gerenciar_comunicados')

    template = (
        'mensagens/comunicados_funcionario.html'
        if is_funcionario(request.user)
        else 'mensagens/mural.html'  # morador, até chegar o design dele
    )
    return render(request, template, _estatisticas_comunicados())


@user_passes_test(is_sindico)
def gerenciar_comunicados(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            return redirect('mensagens:gerenciar_comunicados')
    else:
        form = NoticiaForm()

    contexto = _estatisticas_comunicados()
    contexto['form'] = form
    return render(request, 'mensagens/comunicados_sindico.html', contexto)


@user_passes_test(is_sindico)
def editar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Não foi possível salvar as alterações do comunicado.')
    return redirect('mensagens:gerenciar_comunicados')


@user_passes_test(is_sindico)
def excluir_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    if request.method == 'POST':
        noticia.delete()
    return redirect('mensagens:gerenciar_comunicados')


@user_passes_test(is_sindico)
def gerenciar_ocorrencias(request):
    return render(request, 'mensagens/gerenciar_mensagens.html',
                  _contexto_gerenciar(Mensagem.objects.all(), 'Ocorrências'))

@login_required
def minhas_ocorrencias(request):
    morador = get_morador(request.user)
    if morador is None:
        return redirect('redirecionar_apos_login')

    base = Mensagem.objects.filter(remetente_id=morador.pk).select_related('responsavel')

    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, request.FILES)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.remetente_id = morador.pk
            msg.save()
            return redirect('mensagens:minhas_ocorrencias')
    else:
        form = OcorrenciaForm()

    filtro = request.GET.get('tipo', '')
    lista = base.filter(tipo=filtro) if filtro in Mensagem.Tipo.values else base

    return render(request, 'mensagens/ocorrencias_morador.html', {
        'form': form,
        'ocorrencias': lista,
        'total': lista.count(),
        'qtd_abertas': base.filter(situacao=Mensagem.Situacao.ABERTA).count(),
        'qtd_andamento': base.filter(situacao=Mensagem.Situacao.EM_ANDAMENTO).count(),
        'qtd_resolvidas': base.filter(situacao=Mensagem.Situacao.RESOLVIDA).count(),
        'filtro': filtro,
        'tipos': Mensagem.Tipo.choices,
        'unidade': morador.apartamento.numero,
    })


def _contexto_gerenciar(mensagens, titulo):
    return {
        'mensagens': mensagens.select_related('remetente', 'responsavel'),
        'titulo_pagina': titulo,
        'funcionarios': Funcionario.objects.all(),
        'situacoes': Mensagem.Situacao.choices,
    }

@user_passes_test(is_sindico)
def atualizar_mensagem(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, id_mensagem=mensagem_id)
    if request.method == 'POST':
        situacao = request.POST.get('situacao')
        if situacao in Mensagem.Situacao.values:
            mensagem.situacao = situacao
        responsavel_id = request.POST.get('responsavel')
        mensagem.responsavel = Funcionario.objects.filter(pk=responsavel_id).first() if responsavel_id else None
        mensagem.save()
    return redirect(request.META.get('HTTP_REFERER', 'home_sindico'))