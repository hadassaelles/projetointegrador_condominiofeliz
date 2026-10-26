from datetime import date
from django import forms
from .areas import AREAS_COMUNS
from .models import Reserva

LOCAIS_DISPONIVEIS = [(a['nome'], a['nome']) for a in AREAS_COMUNS]
CAPACIDADES = {a['nome']: a['capacidade'] for a in AREAS_COMUNS}


class ReservaForm(forms.ModelForm):
    local = forms.ChoiceField(choices=LOCAIS_DISPONIVEIS, label='Área comum')

    class Meta:
        model = Reserva
        fields = ['local', 'data', 'horas_ini', 'horas_final', 'quant_pessoas', 'observacoes']
        labels = {
            'data': 'Data da reserva',
            'horas_ini': 'Horário de início',
            'horas_final': 'Horário de término',
            'quant_pessoas': 'Quantidade de pessoas',
            'observacoes': 'Observações (opcional)',
        }
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'horas_ini': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
            'horas_final': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
            'quant_pessoas': forms.NumberInput(attrs={'min': 1}),
            'observacoes': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Informações adicionais para a administração...',
            }),
        }

    def clean_data(self):
        data = self.cleaned_data['data']
        if data < date.today():
            raise forms.ValidationError('Não é possível reservar em uma data passada.')
        return data

    def clean(self):
        cleaned = super().clean()
        local = cleaned.get('local')
        data = cleaned.get('data')
        inicio = cleaned.get('horas_ini')
        fim = cleaned.get('horas_final')
        qtd = cleaned.get('quant_pessoas')

        if inicio and fim and fim <= inicio:
            raise forms.ValidationError('O horário final deve ser depois do inicial.')

        capacidade = CAPACIDADES.get(local)
        if capacidade and qtd and qtd > capacidade:
            self.add_error('quant_pessoas', f'A capacidade máxima de {local} é {capacidade} pessoas.')

        if local and data and inicio and fim:
            conflito = (
                Reserva.objects
                .filter(local=local, data=data, horas_ini__lt=fim, horas_final__gt=inicio)
                .exclude(status=Reserva.Status.CANCELADA)
                .exists()
            )
            if conflito:
                raise forms.ValidationError('Já existe uma reserva para essa área nesse horário.')

        return cleaned