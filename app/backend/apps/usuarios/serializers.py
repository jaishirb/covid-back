from . import models
from backend.apps.utils.serializers import CustomSerializer
from rest_framework import serializers


class UserCovidSerializer(CustomSerializer):
    class Meta:
        model = models.UsuarioCovid
        exclude = [
            'password',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions'
        ]
        extra_fields = [
        ]