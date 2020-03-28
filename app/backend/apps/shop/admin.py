from django.contrib import admin
from .forms import ColorForm
from . import models


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    form = ColorForm
    fieldsets = (
        (None, {
            'fields': ('nombre', 'color')
        }),
    )


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
    ]
    search_fields = [
        'id',
        'nombre'
    ]

    list_filter = [
    ]


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    filter_horizontal = ('colores',)
    list_display = [
        'id',
        'nombre',
        'descripcion',
        'imagen',
        'precio',
        'categoria',
    ]
    search_fields = [
        'id',
        'nombre',
        'precio'
    ]

    list_filter = [
        'categoria'
    ]


@admin.register(models.PedidoIndividual)
class PedidoIndividualAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'producto',
        'color',
        'cantidad',
    ]
    search_fields = [
        'id',
        'producto__nombre',
    ]

    list_filter = [
        'producto__categoria'
    ]


@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    filter_horizontal = ('pedidos_individuales',)
    list_display = [
        'id',
        'domicilio_cliente',
        'telefono_cliente',
        'nombre_cliente',
        'total',
        'estado'
    ]
    search_fields = [
        'id',
        'domicilio_cliente',
        'telefono_cliente',
        'nombre_cliente',
        'total'
    ]

    list_filter = [
        'estado'
    ]


@admin.register(models.Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'producto',
        'stock',
        'disponible',
        'ultima_modificacion',
        'vendidos',
        'total_ventas'
    ]
    search_fields = [
        'id',
        'producto__nombre',
        'vendidos',
        'total_ventas',
        'stock'
    ]

    list_filter = [
        'disponible',
        'ultima_modificacion'
    ]
