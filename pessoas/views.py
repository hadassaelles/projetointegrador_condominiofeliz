from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .permissions import is_sindico

@user_passes_test(is_sindico)
def home_sindico(request):
    return render(request, 'pessoas/home_sindico.html')