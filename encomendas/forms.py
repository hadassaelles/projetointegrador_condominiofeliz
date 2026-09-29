from django import forms
from django.contrib.auth.models import User
from .models import Encomenda

class EncomendaForm(forms.ModelForm):
    morador = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=False).order_by('username'),
        label='Morador'
    )

    class Meta:
        model = Encomenda
        fields = ['morador', 'unidade', 'descricao']