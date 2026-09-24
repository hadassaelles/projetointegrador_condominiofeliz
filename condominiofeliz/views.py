from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def home(request):
    pessoa = getattr(request.user, 'pessoa', None)

    if pessoa is None:
        return redirect('login')

    if hasattr(pessoa, 'morador'):
        return render(request, 'homeMorador.html')
    elif hasattr(pessoa, 'sindico'):
        return render(request, 'homeSindico.html')
    elif hasattr(pessoa, 'funcionario'):
        return render(request, 'homeFuncionario.html')
    else:
        return redirect('login')

@login_required
def ocorrencia_morador(request):
    return render(request, 'ocorrenciaMorador.html')

@login_required
def abrir_ocorrencia(request):
    pessoa = getattr(request.user, 'pessoa', None)
    morador = getattr(pessoa, 'morador', None) if pessoa else None

    if morador is None:
        return redirect('login')

    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        foto = request.FILES.get('fotos')

        sindico = morador.apartamento.sindico
        if sindico is None:
            messages.error(request, 'Não há síndico cadastrado para o seu apartamento.')
            return redirect('abrir_ocorrencia')

        Mensagem.objects.create(
            emissor=morador,
            receptor=sindico,
            tipo=categoria,
            texto=f"{titulo}\n\n{descricao}",
            imagem=foto,
            situacao='enviada',
        )

        return redirect('ocorrencias_morador')
    return render (request, 'abrirOcorrenciaMorador.html')