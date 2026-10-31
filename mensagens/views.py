from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from pessoas.models import Funcionario
from pessoas.permissions import is_sindico, is_funcionario, get_morador
from .models import Comunicado, Ocorrencia
from .forms import ComunicadoForm, OcorrenciaForm


# ---------------------------------------------------------------------------
# Comunicados (Mural)
# ---------------------------------------------------------------------------

def _estatisticas_comunicados():
    sete_dias = timezone.now() - timedelta(days=7)
    comunicados = Comunicado.objects.select_related('autor')
    return {
        'noticias': comunicados,       # nome antigo, mantido para os templates
        'comunicados': comunicados,
        'novos_7_dias': comunicados.filter(criado_em__gte=sete_dias).count(),
        'total': comunicados.count(),
    }


@login_required
def mural(request):
    if is_sindico(request.user):
        return redirect('mensagens:gerenciar_comunicados')

    template = (
        'mensagens/comunicados_funcionario.html'
        if is_funcionario(request.user)
        else 'mensagens/comunicados_morador.html'
    )
    return render(request, template, _estatisticas_comunicados())


@user_passes_test(is_sindico)
def gerenciar_comunicados(request):
    if request.method == 'POST':
        form = ComunicadoForm(request.POST)
        if form.is_valid():
            comunicado = form.save(commit=False)
            comunicado.autor = request.user
            comunicado.save()
            return redirect('mensagens:gerenciar_comunicados')
    else:
        form = ComunicadoForm()

    contexto = _estatisticas_comunicados()
    contexto['form'] = form
    return render(request, 'mensagens/comunicados_sindico.html', contexto)


@user_passes_test(is_sindico)
def editar_noticia(request, noticia_id):
    comunicado = get_object_or_404(Comunicado, id=noticia_id)
    if request.method == 'POST':
        form = ComunicadoForm(request.POST, instance=comunicado)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Não foi possível salvar as alterações do comunicado.')
    return redirect('mensagens:gerenciar_comunicados')


@user_passes_test(is_sindico)
def excluir_noticia(request, noticia_id):
    comunicado = get_object_or_404(Comunicado, id=noticia_id)
    if request.method == 'POST':
        comunicado.delete()
    return redirect('mensagens:gerenciar_comunicados')


# ---------------------------------------------------------------------------
# Ocorrências
# ---------------------------------------------------------------------------

def _contexto_ocorrencias(base, filtro):
    """Monta a parte do contexto que é igual para síndico e morador."""
    lista = base.filter(categoria=filtro) if filtro in Ocorrencia.Categoria.values else base
    return {
        'ocorrencias': lista,
        'total': lista.count(),
        'qtd_abertas': base.filter(status=Ocorrencia.Status.ABERTA).count(),
        'qtd_andamento': base.filter(status=Ocorrencia.Status.EM_ANDAMENTO).count(),
        'qtd_resolvidas': base.filter(status=Ocorrencia.Status.RESOLVIDA).count(),
        'filtro': filtro,
        'tipos': Ocorrencia.Categoria.choices,
    }


@user_passes_test(is_sindico)
def gerenciar_ocorrencias(request):
    base = Ocorrencia.objects.select_related('morador__morador__apartamento', 'responsavel')
    filtro = request.GET.get('tipo', '')

    contexto = _contexto_ocorrencias(base, filtro)
    contexto['funcionarios'] = Funcionario.objects.all()
    contexto['situacoes'] = Ocorrencia.Status.choices
    return render(request, 'mensagens/ocorrencias_sindico.html', contexto)


@login_required
def minhas_ocorrencias(request):
    morador = get_morador(request.user)
    if morador is None:
        return redirect('redirecionar_apos_login')

    base = Ocorrencia.objects.filter(morador_id=morador.pk).select_related('responsavel')

    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, request.FILES)
        if form.is_valid():
            ocorrencia = form.save(commit=False)
            ocorrencia.morador_id = morador.pk
            ocorrencia.unidade = str(morador.apartamento.numero)
            ocorrencia.save()
            return redirect('mensagens:minhas_ocorrencias')
    else:
        form = OcorrenciaForm()

    filtro = request.GET.get('tipo', '')
    contexto = _contexto_ocorrencias(base, filtro)
    contexto['form'] = form
    contexto['unidade'] = morador.apartamento.numero
    return render(request, 'mensagens/ocorrencias_morador.html', contexto)


@user_passes_test(is_sindico)
def atualizar_mensagem(request, mensagem_id):
    """Atualiza status e responsável de uma ocorrência.

    O parâmetro continua se chamando mensagem_id para não quebrar o urls.py.
    """
    ocorrencia = get_object_or_404(Ocorrencia, id_ocorrencia=mensagem_id)
    if request.method == 'POST':
        status = request.POST.get('situacao')
        if status in Ocorrencia.Status.values:
            ocorrencia.status = status

        responsavel_id = request.POST.get('responsavel')
        ocorrencia.responsavel = (
            Funcionario.objects.filter(pk=responsavel_id).first() if responsavel_id else None
        )
        ocorrencia.save()
    return redirect(request.META.get('HTTP_REFERER', 'home_sindico'))