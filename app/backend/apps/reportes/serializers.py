from datetime import datetime, timedelta
from . import models
from backend.apps.utils.serializers import CustomSerializer
from rest_framework import serializers

from ..utils.shortcuts import get_object_or_none


class TipoNecesidadSerializer(CustomSerializer):

    class Meta:
        model = models.TipoNecesidad
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]


class ReporteNecesidadSerializer(CustomSerializer):
    ubicaciones = serializers.ReadOnlyField(source='get_ubicaciones')

    class Meta:
        model = models.ReporteNecesidad
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
            'ubicaciones'
        ]

    def create(self, validate_data):
        if not self.context['request'].user.is_anonymous:
            email_usuario = self.context['request'].user.email
            usuario = get_object_or_none(models.UsuarioCovid, email=email_usuario)
            if usuario:
                validate_data['usuario'] = usuario
                instance = models.ReporteNecesidad.objects.create(
                    **validate_data
                )
                return instance
            raise serializers.ValidationError({'error': 'El usuario no es de tipo covid.'})
        raise serializers.ValidationError({'error': 'El usuario debe estar autenticado.'})


class UbicacionesNecesidadSerializer(CustomSerializer):
    class Meta:
        model = models.UbicacionesNecesidad
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]
