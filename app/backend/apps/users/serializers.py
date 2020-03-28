from . import models
from backend.apps.utils.serializers import CustomSerializer
from rest_framework import serializers


class UserPettiSerializer(CustomSerializer):
    photo_read = serializers.FileField(read_only=True, source='get_image')
    class Meta:
        model = models.UserPetti
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
            'photo_read'
        ]
