from datetime import datetime, timedelta

from . import models
from backend.apps.utils.serializers import CustomSerializer
from rest_framework import serializers


class CategoriaSerializer(CustomSerializer):
    class Meta:
        model = models.Categoria
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]


class ColorSerializer(CustomSerializer):
    class Meta:
        model = models.Color
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]


class ProductoSerializer(CustomSerializer):
    categoria_read = serializers.ReadOnlyField(source='categoria.nombre')
    precio_read = serializers.ReadOnlyField(source='get_precio')
    colores = ColorSerializer(many=True, read_only=True)

    class Meta:
        model = models.Producto
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
            'categoria_read',
            'precio_read',
            'colores'
        ]


class PedidoIndividualSerializer(CustomSerializer):
    producto_read = serializers.ReadOnlyField(source='producto.nombre')

    class Meta:
        model = models.PedidoIndividual
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
            'producto_read'
        ]


class PedidoSerializer(CustomSerializer):
    pedidos_individuales = PedidoIndividualSerializer(many=True)

    class Meta:
        model = models.Pedido
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
            'pedidos_individuales'
        ]

    def create(self, validate_data):
        if not self.context['request'].user.is_anonymous:
            pedidos_validated_data = validate_data.pop('pedidos_individuales')
            if len(pedidos_validated_data) == 0:
                raise serializers.ValidationError({'error': 'Pedidos can not be empty.'})
            else:
                fix = super().create(validate_data)
                fixes_set_serializer = self.fields['pedidos_individuales']
                fixes_rule_server_relations = list(fixes_set_serializer.create(pedidos_validated_data))
                fix.pedidos_individuales.add(*fixes_rule_server_relations)
                fix.fecha_entrega = datetime.now().date() + timedelta(days=1)
                fix.save()
                return fix
        raise serializers.ValidationError({'error': 'El usuario debe estar autenticado.'})


class InventarioSerializer(CustomSerializer):
    producto_read = serializers.ReadOnlyField(source='producto.nombre')

    class Meta:
        model = models.Inventario
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
            'producto_read'
        ]
