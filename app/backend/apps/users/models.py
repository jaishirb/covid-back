from django.db import models

from backend.apps.utils.models import ModelBase
from django.contrib.auth.models import User


class UserPetti(User):
    photo = models.ForeignKey(
        'mascotas.Imagen',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    telefono = models.CharField(
        max_length=45,
        blank=True,
        null=True
    )
    direccion = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    ciudad = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )


    def __str__(self):
        return "{}".format(self.email)

    def get_image(self):
        if self.photo:
            return self.photo.photo
        return None

    class Meta:
        verbose_name = 'User Petti'
        verbose_name_plural = 'Users Petti'