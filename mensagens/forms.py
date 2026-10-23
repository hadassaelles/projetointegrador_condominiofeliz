from django import forms
from .models import Noticia, Mensagem


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'categoria', 'prioridade', 'conteudo']
        labels = {'titulo': 'Título do comunicado', 'conteudo': 'Mensagem / Detalhes'}
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': "Ex: Manutenção na bomba d'água"}),
            'conteudo': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Escreva a mensagem que os moradores irão visualizar...',
            }),
        }


class OcorrenciaForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=Mensagem.Tipo.choices, label='Categoria')

    class Meta:
        model = Mensagem
        fields = ['titulo', 'tipo', 'texto', 'imagem']
        labels = {'titulo': 'Título', 'texto': 'Descrição', 'imagem': 'Foto (opcional)'}
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ex: Vazamento na garagem'}),
            'texto': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva o problema em detalhes...'}),
        }