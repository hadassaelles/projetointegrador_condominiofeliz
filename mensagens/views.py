from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from pessoas.permissions import is_sindico, _get_pessoa
from .models import Noticia, Mensagem
from .forms import NoticiaForm, OcorrenciaForm, SugestaoForm

@login_required
def mural(request):
    noticias = Noticia.objects.all()
    return render(request, 'mensagens/mural.html', {
        'noticias': noticias,
        'is_sindico_flag': is_sindico(request.user),
    })


@user_passes_test(is_sindico)
def publicar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            return redirect('mensagens:mural')
    else:
        form = NoticiaForm()
    return render(request, 'mensagens/noticia_form.html', {'form': form, 'titulo_pagina': 'Publicar Comunicado'})


@user_passes_test(is_sindico)
def editar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('mensagens:mural')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'mensagens/noticia_form.html', {'form': form, 'titulo_pagina': 'Editar Comunicado'})


@user_passes_test(is_sindico)
def excluir_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    if request.method == 'POST':
        noticia.delete()
        return redirect('mensagens:mural')
    return render(request, 'mensagens/noticia_confirmar_exclusao.html', {'noticia': noticia})

@user_passes_test(is_sindico)
def resolver_mensagem(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, id_mensagem=mensagem_id)
    if request.method == 'POST':
        mensagem.situacao = Mensagem.Situacao.RESOLVIDA
        mensagem.save()
    return redirect(request.META.get('HTTP_REFERER', 'home_sindico'))


@login_required
def nova_ocorrencia(request):
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, request.FILES)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.remetente = get_pessoa(request.user)
            msg.save()
            return redirect('home_morador')
    else:
        form = OcorrenciaForm()
    return render(request, 'mensagens/mensagem_form.html', {'form': form, 'titulo_pagina': 'Reclamação / Denúncia'})


@login_required
def nova_sugestao(request):
    if request.method == 'POST':
        form = SugestaoForm(request.POST, request.FILES)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.remetente = get_pessoa(request.user)
            msg.tipo = Mensagem.Tipo.SUGESTAO
            msg.save()
            return redirect('home_morador')
    else:
        form = SugestaoForm()
    return render(request, 'mensagens/mensagem_form.html', {'form': form, 'titulo_pagina': 'Sugestão'})


@user_passes_test(is_sindico)
def gerenciar_ocorrencias(request):
    mensagens = Mensagem.objects.filter(tipo__in=[Mensagem.Tipo.RECLAMACAO, Mensagem.Tipo.DENUNCIA])
    return render(request, 'mensagens/gerenciar_mensagens.html', {'mensagens': mensagens, 'titulo_pagina': 'Reclamações e Denúncias'})


@user_passes_test(is_sindico)
def gerenciar_sugestoes(request):
    mensagens = Mensagem.objects.filter(tipo=Mensagem.Tipo.SUGESTAO)
    return render(request, 'mensagens/gerenciar_mensagens.html', {'mensagens': mensagens, 'titulo_pagina': 'Sugestões'})