from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from pessoas.permissions import is_sindico
from .models import Noticia
from .forms import NoticiaForm


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