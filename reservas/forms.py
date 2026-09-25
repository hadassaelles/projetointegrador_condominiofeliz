from datetime import date
from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['area', 'data', 'hora_inicio', 'hora_fim', 'unidade']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fim': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_data(self):
        data = self.cleaned_data['data']
        if data < date.today():
            raise forms.ValidationError('Não é possível reservar em uma data passada.')
        return data

    def clean(self):
        cleaned = super().clean()
        inicio = cleaned.get('hora_inicio')
        fim = cleaned.get('hora_fim')
        if inicio and fim and fim <= inicio:
            raise forms.ValidationError('O horário final deve ser depois do inicial.')
        return cleaned