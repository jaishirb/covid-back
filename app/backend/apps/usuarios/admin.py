from django.contrib import admin
from . import models


@admin.register(models.UsuarioCovid)
class UsuariosCovidAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'cedula',
        'email',
        'telefono',
        'edad',
        'direccion',
        'ubicacion',
        'rol_usuario'
    ]
    search_fields = [
        'id',
        'username',
        'email',
        'telefono',
        'cedula'
    ]

    list_filter = [
    ]


@admin.register(models.RolUsuario)
class RolUsuarioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'descripcion',
    ]
    search_fields = [
        'id',
    ]

    list_filter = [
    ]
