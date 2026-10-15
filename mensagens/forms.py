from django import forms
from .models import Noticia, Mensagem

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo']

class OcorrenciaForm(forms.ModelForm):
    tipo = forms.ChoiceField(
        choices=[(Mensagem.Tipo.RECLAMACAO, 'Reclamação'), (Mensagem.Tipo.DENUNCIA, 'Denúncia')],
        label='Tipo'
    )

    class Meta:
        model = Mensagem
        fields = ['tipo', 'texto', 'imagem']


class SugestaoForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['texto', 'imagem']