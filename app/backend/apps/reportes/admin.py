from django.contrib import admin, messages
from . import models


# Register your models here.
@admin.register(models.TipoNecesidad)
class TipoNecesidadAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
    ]
    search_fields = [
        'nombre',
    ]

    list_filter = [
    ]


@admin.register(models.ReporteCovid)
class ReporteCovidAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'edad',
        'identificacion',
        'tipo_persona',
        'usuario',
    ]
    search_fields = [
        'usuario',
        'nombre',
        'identificacion'
    ]

    list_filter = [
        'tipo_persona',
        'edad'
    ]


@admin.register(models.UbicacionesCovid)
class UbicacionesCovidAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fecha',
        'direccion',
        'ubicacion',
        'reporte_covid',
    ]
    search_fields = [
        'direccion',
    ]

    list_filter = [
        'fecha',
    ]


@admin.register(models.ReporteNecesidad)
class ReporteNecesidadAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'descripcion',
        'tipo_necesidad',
        'nombre',
        'edad',
        'telefono',
        'tipo_persona'
    ]
    search_fields = [
        'nombre',
    ]

    list_filter = [
        'tipo_necesidad',
        'tipo_persona',
        'edad'
    ]


@admin.register(models.UbicacionesNecesidad)
class UbicacionesNecesidadAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fecha',
        'direccion',
        'ubicacion',
        'reporte_necesidad',
    ]
    search_fields = [
        'direccion',
    ]

    list_filter = [
        'fecha',
    ]
