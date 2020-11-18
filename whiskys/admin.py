from django.contrib import admin

from .models import Whisky, Avaliacao


@admin.register(Whisky)
class WhiskyAdmin(admin.ModelAdmin):
    list_display = ('nome', 'type', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('whisky', 'avaliador', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')