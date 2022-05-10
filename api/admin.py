from django.contrib import admin
from .models import Arma, Municao, Objeto, ObjetoTipo


@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'calibre')


@admin.register(Municao)
class MunicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'calibre')


@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'objeto_tipo')


@admin.register(ObjetoTipo)
class ObjetoTipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_de_objeto')
