from django import forms
from .models import Comunicado, Ocorrencia


class ComunicadoForm(forms.ModelForm):
    class Meta:
        model = Comunicado
        fields = ['titulo', 'conteudo']


# Alias para retrocompatibilidade
NoticiaForm = ComunicadoForm


class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['categoria', 'titulo', 'descricao', 'unidade', 'imagem']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }