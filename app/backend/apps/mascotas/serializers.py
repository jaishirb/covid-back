from . import models
from backend.apps.utils.serializers import CustomSerializer
from rest_framework import serializers

from ..users.serializers import UserPettiSerializer
from ..utils.shortcuts import get_object_or_none


class MascotaSerializer(CustomSerializer):
    class Meta:
        model = models.Mascota
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]


class ImagenSerializer(CustomSerializer):
    usuario_read = serializers.ReadOnlyField(source='usuario.username')
    class Meta:
        model = models.Imagen
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
            'usuario_read'
        ]

    def create(self, validate_data):
        if not self.context['request'].user.is_anonymous:
            usuario = get_object_or_none(models.UserPetti, id=self.context['request'].user.id)
            validate_data['usuario'] = usuario
            return super().create(validate_data)
        raise serializers.ValidationError({'error': 'El usuario debe estar autenticado.'})


class PublicacionSerializer(CustomSerializer):
    username = serializers.ReadOnlyField(source='usuario.username')
    media_url_read = serializers.FileField(read_only=True, source='get_image')
    telefono = serializers.ReadOnlyField(source='usuario.telefono')
    image_profile = serializers.FileField(read_only=True, source='get_user_image')

    class Meta:
        model = models.Publicacion
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
            'username',
            'media_url_read',
            'telefono',
            'image_profile'
        ]

    def create(self, validate_data):
        if not self.context['request'].user.is_anonymous:
            validate_data['likes'] = {}
            usuario = get_object_or_none(models.UserPetti, id=self.context['request'].user.id)
            validate_data['usuario'] = usuario
            return super().create(validate_data)
        raise serializers.ValidationError({'error': 'El usuario debe estar autenticado.'})


class EmpresaSerializer(CustomSerializer):
    class Meta:
        model = models.Empresa
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]


class ServicioEmpresaSerializer(CustomSerializer):
    precio_read = serializers.ReadOnlyField(source='get_precio')
    foto_empresa = serializers.FileField(read_only=True, source='empresa.foto')
    nombre_empresa = serializers.ReadOnlyField(source='empresa.nombre')
    direccion_empresa = serializers.ReadOnlyField(source='empresa.direccion')

    class Meta:
        model = models.ServicioEmpresa
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
            'get_precio',
            'foto_empresa',
            'nombre_empresa',
            'direccion_empresa'
        ]


class ReservaSerializer(CustomSerializer):
    class Meta:
        model = models.Reserva
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]

    def create(self, validate_data):
        if not self.context['request'].user.is_anonymous:
            usuario = get_object_or_none(models.UserPetti, id=self.context['request'].user.id)
            validate_data['usuario'] = usuario
            return super().create(validate_data)
        raise serializers.ValidationError({'error': 'El usuario debe estar autenticado.'})
