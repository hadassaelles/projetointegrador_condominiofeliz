from datetime import date
from django import forms
from .models import Reserva

LOCAIS_DISPONIVEIS = [
    ('Salão de Festas', '🎉 Salão de Festas'),
    ('Churrasqueira', '🔥 Churrasqueira'),
    ('Quadra Poliesportiva', '🏆 Quadra Poliesportiva'),
    ('Piscina', '🌊 Piscina'),
]


class ReservaForm(forms.ModelForm):
    local = forms.ChoiceField(choices=LOCAIS_DISPONIVEIS, label='Área')

    class Meta:
        model = Reserva
        fields = ['local', 'data', 'horas_ini', 'horas_final', 'quant_pessoas']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horas_ini': forms.TimeInput(attrs={'type': 'time'}),
            'horas_final': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_data(self):
        data = self.cleaned_data['data']
        if data < date.today():
            raise forms.ValidationError('Não é possível reservar em uma data passada.')
        return data

    def clean(self):
        cleaned = super().clean()
        inicio = cleaned.get('horas_ini')
        fim = cleaned.get('horas_final')
        if inicio and fim and fim <= inicio:
            raise forms.ValidationError('O horário final deve ser depois do inicial.')
        return cleaned