from django.contrib import admin
from . import models


@admin.register(models.Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'photo',
        'created',
        'usuario',
    ]
    search_fields = [
        'id',
        'title'
    ]

    list_filter = [
        'created'
    ]


@admin.register(models.Mascota)
class MascotaAdmin(admin.ModelAdmin):
    filter_horizontal = ('fotos',)
    list_display = [
        'id',
        'ciudad',
        'descripcion',
        'raza',
        'edad'
    ]
    search_fields = [
        'id',
        'ciudad',
    ]

    list_filter = [
        'raza'
    ]


@admin.register(models.Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'description',
        'tag',
        'location',
        'media_url',
        'likes',
        'timestamp',
        'usuario'
    ]
    search_fields = [
        'id',
        'location',
        'usuario'
    ]

    list_filter = [
        'timestamp',
        'tag'
    ]


@admin.register(models.Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'direccion',
        'telefono',
        'correo',
        'foto'
    ]
    search_fields = [
        'id',
        'nombre',
        'direccion',
        'telefono',
        'email'
    ]

    list_filter = [
    ]


@admin.register(models.ServicioEmpresa)
class ServicioEmpresaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'precio',
        'descripcion',
        'background',
        'empresa'
    ]
    search_fields = [
        'id',
        'nombre',
    ]

    list_filter = [
        'empresa'
    ]


@admin.register(models.Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'usuario',
        'servicio',
        'estado',
    ]
    search_fields = [
        'id',
        'servicio__nombre',
        'usuario__correo'
    ]

    list_filter = [
        'estado'
    ]

