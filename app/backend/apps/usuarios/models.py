from django.contrib.auth.models import User
from django.contrib.gis.db import models

from backend.apps.utils.models import ModelBase


class RolUsuario(ModelBase):
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Rol usuario'
        verbose_name_plural = 'Rol usuarios'


class UsuarioCovid(User):
    cedula = models.CharField(max_length=45)
    edad = models.PositiveIntegerField()
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=120)
    ubicacion = models.PointField(
        blank=True,
        null=True
    )
    rol_usuario = models.ForeignKey(
        RolUsuario,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario Covid'
        verbose_name_plural = 'Usuarios Covid'
