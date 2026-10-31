from django import forms
from pessoas.models import Morador
from .models import Encomenda

DATETIME_LOCAL = '%Y-%m-%dT%H:%M'


class MoradorChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.nome} {obj.sobrenome} — Apto {obj.apartamento.numero}'


class EncomendaForm(forms.ModelForm):
    morador = MoradorChoiceField(
        queryset=Morador.objects.select_related('apartamento').order_by('nome'),
        label='Morador',
        empty_label='Selecione o morador',
    )
    recebido_em = forms.DateTimeField(
        label='Data e hora do recebimento',
        input_formats=[DATETIME_LOCAL],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format=DATETIME_LOCAL),
    )

    class Meta:
        model = Encomenda
        fields = ['descricao', 'morador', 'recebido_em']
        labels = {'descricao': 'Descrição'}
        widgets = {
            'descricao': forms.TextInput(attrs={'placeholder': 'Ex.: Pacote Amazon (Caixa Média)'}),
        }