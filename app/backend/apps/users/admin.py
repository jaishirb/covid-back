from django.contrib import admin
from . import models


@admin.register(models.UserPetti)
class UsuariosPettiAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'email',
        'telefono',
        'direccion',
        'photo'
    ]
    search_fields = [
        'id',
        'username',
        'email',
        'telefono',
        'direccion'
    ]

    list_filter = [
    ]
