from django.contrib import admin

# Register your models here.
from . import models


class CaoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('no_usuario', 'ds_senha')


class PermissaoSistemaAdmin(admin.ModelAdmin):
    list_display = ('co_usuario', 'in_ativo')


class CaoFaturaAdmin(admin.ModelAdmin):
    list_display = (
        'co_fatura', 'co_cliente', 'co_sistema', 'co_os', 'data_emissao')


class CaoOsAdmin(admin.ModelAdmin):
    list_display = ('co_os', 'co_usuario', 'ds_os', 'ds_caracteristica')


class CaoSistemaAdmin(admin.ModelAdmin):
    list_display = ('co_sistema', 'no_sistema', 'ds_caracteristica')

admin.site.register(models.CaoUsuario, CaoUsuarioAdmin)
admin.site.register(models.PermissaoSistema, PermissaoSistemaAdmin)
admin.site.register(models.CaoOs, CaoOsAdmin)
admin.site.register(models.CaoFatura, CaoFaturaAdmin)
admin.site.register(models.CaoSistema, CaoSistemaAdmin)
