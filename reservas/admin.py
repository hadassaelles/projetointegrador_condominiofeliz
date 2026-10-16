from django.contrib import admin
from .models import Area, Reserva, Convidado

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'capacidade', 'icone')

class ConvidadoInline(admin.TabularInline):
    model = Convidado
    extra = 1

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('area', 'morador', 'unidade', 'data', 'hora_inicio', 'hora_fim', 'status')
    list_filter = ('status', 'data', 'area')
    inlines = [ConvidadoInline]

@admin.register(Convidado)
class ConvidadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'reserva')
    search_fields = ('nome',)

