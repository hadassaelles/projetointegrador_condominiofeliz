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