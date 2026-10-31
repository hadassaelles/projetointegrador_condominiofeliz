from django import forms
from .models import Comunicado, Ocorrencia


class ComunicadoForm(forms.ModelForm):
    """Formulário para criar/editar um Comunicado (Mural)."""

    class Meta:
        model = Comunicado
        fields = ['titulo', 'conteudo']
        labels = {
            'titulo': 'Título do comunicado',
            'conteudo': 'Mensagem / Detalhes',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': "Ex: Manutenção na bomba d'água"}),
            'conteudo': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Escreva a mensagem que os moradores irão visualizar...',
            }),
        }


# Alias para não quebrar imports antigos
NoticiaForm = ComunicadoForm


class OcorrenciaForm(forms.ModelForm):
    """Formulário usado pelo morador para abrir uma ocorrência."""

    class Meta:
        model = Ocorrencia
        fields = ['titulo', 'categoria', 'descricao', 'imagem']
        labels = {
            'titulo': 'Título',
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'imagem': 'Foto (opcional)',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ex: Vazamento na garagem'}),
            'descricao': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Descreva o problema em detalhes...',
            }),
        }