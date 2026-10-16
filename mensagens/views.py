from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from pessoas.permissions import is_sindico, is_morador
from pessoas.models import Pessoa
from .models import Comunicado, Ocorrencia
from .forms import ComunicadoForm, OcorrenciaForm


def get_user_pessoa(user):
    """Obtém ou vincula a Pessoa correspondente ao User autenticado."""
    if hasattr(user, 'pessoa'):
        return user.pessoa
    pessoa, _ = Pessoa.objects.get_or_create(
        user=user,
        defaults={
            'nome': user.first_name or user.username,
            'sobrenome': user.last_name or '',
            'cpf': f'{user.id:011d}'[-14:],
            'email': user.email or f'{user.username}@condominio.local',
        }
    )
    return pessoa


# ==========================================
# COMUNICADOS (Mural do Síndico)
# ==========================================

@login_required
def mural(request):
    comunicados = Comunicado.objects.all()
    return render(request, 'mensagens/mural.html', {
        'noticias': comunicados,
        'comunicados': comunicados,
        'is_sindico_flag': is_sindico(request.user),
    })


@user_passes_test(is_sindico)
def publicar_noticia(request):
    if request.method == 'POST':
        form = ComunicadoForm(request.POST)
        if form.is_valid():
            comunicado = form.save(commit=False)
            comunicado.autor = request.user
            comunicado.save()
            return redirect('mensagens:mural')
    else:
        form = ComunicadoForm()
    return render(request, 'mensagens/noticia_form.html', {'form': form, 'titulo_pagina': 'Publicar Comunicado'})


@user_passes_test(is_sindico)
def editar_noticia(request, noticia_id):
    comunicado = get_object_or_404(Comunicado, id=noticia_id)
    if request.method == 'POST':
        form = ComunicadoForm(request.POST, instance=comunicado)
        if form.is_valid():
            form.save()
            return redirect('mensagens:mural')
    else:
        form = ComunicadoForm(instance=comunicado)
    return render(request, 'mensagens/noticia_form.html', {'form': form, 'titulo_pagina': 'Editar Comunicado'})


@user_passes_test(is_sindico)
def excluir_noticia(request, noticia_id):
    comunicado = get_object_or_404(Comunicado, id=noticia_id)
    if request.method == 'POST':
        comunicado.delete()
        return redirect('mensagens:mural')
    return render(request, 'mensagens/noticia_confirmar_exclusao.html', {'noticia': comunicado})


# ==========================================
# OCORRÊNCIAS (Morador e Síndico)
# ==========================================

@login_required
def minhas_ocorrencias(request):
    """Listagem de ocorrências do morador logado."""
    pessoa = get_user_pessoa(request.user)
    morador = getattr(pessoa, 'morador', None)

    todas_minhas = Ocorrencia.objects.filter(morador=pessoa)
    categoria_filtro = request.GET.get('categoria', '').strip()
    if categoria_filtro:
        ocorrencias = todas_minhas.filter(categoria=categoria_filtro)
    else:
        ocorrencias = todas_minhas

    context = {
        'ocorrencias': ocorrencias,
        'total_todas': todas_minhas.count(),
        'total_abertas': todas_minhas.filter(status=Ocorrencia.Status.ABERTA).count(),
        'total_em_andamento': todas_minhas.filter(status=Ocorrencia.Status.EM_ANDAMENTO).count(),
        'total_resolvidas': todas_minhas.filter(status=Ocorrencia.Status.RESOLVIDA).count(),
        'categoria_selecionada': categoria_filtro,
        'morador': morador,
        'pessoa': pessoa,
    }
    return render(request, 'pessoas/morador/ocorrencia.html', context)


@login_required
def nova_ocorrencia(request):
    """Formulário para o morador abrir uma nova ocorrência."""
    pessoa = get_user_pessoa(request.user)
    morador = getattr(pessoa, 'morador', None)
    unidade_padrao = f"Apto {morador.apartamento.numero}" if (morador and morador.apartamento) else ""

    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, request.FILES)
        if form.is_valid():
            ocorrencia = form.save(commit=False)
            ocorrencia.morador = pessoa
            if not ocorrencia.unidade and unidade_padrao:
                ocorrencia.unidade = unidade_padrao
            ocorrencia.status = Ocorrencia.Status.ABERTA
            ocorrencia.save()
            messages.success(request, 'Ocorrência registrada com sucesso!')
            return redirect('mensagens:minhas_ocorrencias')
    else:
        form = OcorrenciaForm(initial={'unidade': unidade_padrao})

    return render(request, 'mensagens/nova_ocorrencia.html', {
        'form': form,
        'morador': morador,
        'pessoa': pessoa,
    })


@user_passes_test(is_sindico)
def gerenciar_ocorrencias(request):
    """Visão do Síndico: todas as ocorrências de todos os moradores."""
    todas = Ocorrencia.objects.select_related('morador', 'responsavel').all()
    categoria_filtro = request.GET.get('categoria', '').strip()
    status_filtro = request.GET.get('status', '').strip()

    ocorrencias = todas
    if categoria_filtro:
        ocorrencias = ocorrencias.filter(categoria=categoria_filtro)
    if status_filtro:
        ocorrencias = ocorrencias.filter(status=status_filtro)

    context = {
        'ocorrencias': ocorrencias,
        'total_todas': todas.count(),
        'total_abertas': todas.filter(status=Ocorrencia.Status.ABERTA).count(),
        'total_em_andamento': todas.filter(status=Ocorrencia.Status.EM_ANDAMENTO).count(),
        'total_resolvidas': todas.filter(status=Ocorrencia.Status.RESOLVIDA).count(),
        'categoria_selecionada': categoria_filtro,
        'status_selecionado': status_filtro,
    }
    return render(request, 'mensagens/gerenciar_ocorrencias.html', context)


@user_passes_test(is_sindico)
def atualizar_status_ocorrencia(request, ocorrencia_id):
    """Síndico atualiza o status de uma ocorrência."""
    ocorrencia = get_object_or_404(Ocorrencia, id_ocorrencia=ocorrencia_id)
    if request.method == 'POST':
        novo_status = request.POST.get('status')
        if novo_status in Ocorrencia.Status.values:
            ocorrencia.status = novo_status
            pessoa_sindico = get_user_pessoa(request.user)
            ocorrencia.responsavel = pessoa_sindico
            ocorrencia.save()
            messages.success(request, f'Ocorrência #{ocorrencia.id_ocorrencia} atualizada para {ocorrencia.get_status_display()}!')
    return redirect('mensagens:gerenciar_ocorrencias')