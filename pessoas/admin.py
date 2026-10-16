from django.contrib import admin
from .models import Pessoa, Telefone, Morador, Sindico, Funcionario


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'email', 'user')
    search_fields = ('nome', 'sobrenome', 'cpf', 'email')
    inlines = [TelefoneInline]


@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'apartamento', 'cpf', 'email')
    search_fields = ('nome', 'sobrenome', 'cpf')
    inlines = [TelefoneInline]


@admin.register(Sindico)
class SindicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'email')
    inlines = [TelefoneInline]


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cargo', 'sindico_responsavel')
    list_filter = ('cargo',)
    inlines = [TelefoneInline]
