from django.contrib import admin
from .models import Pessoa, Telefone, Morador, Sindico, Funcionario

admin.site.register(Pessoa)
admin.site.register(Telefone)
admin.site.register(Morador)
admin.site.register(Sindico)
admin.site.register(Funcionario)
