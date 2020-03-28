from django.db import models
from django.contrib.postgres.fields import JSONField

from backend.apps.users.models import UserPetti
from backend.apps.utils.constants import STATUS, TAGS
from backend.apps.utils.models import ModelBase
from django.contrib.humanize.templatetags.humanize import intcomma


class Imagen(ModelBase):
    title = models.CharField(max_length=100)
    photo = models.FileField(upload_to='images')
    usuario = models.ForeignKey(
        UserPetti,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'


class Mascota(ModelBase):
    fotos = models.ManyToManyField(Imagen)
    ciudad = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    descripcion = models.TextField(
        blank=True,
        null=True
    )
    raza = models.CharField(
        max_length=45
    )
    edad = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return "{} {}".format(self.raza, str(self.id))

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'


class BasePost(ModelBase):
    description = models.TextField(
        blank=True,
        null=True
    )
    location = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    media_url = models.ForeignKey(
        Imagen,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True


class Publicacion(BasePost):
    likes = JSONField(
        blank=True,
        null=True
    )
    tag = models.CharField(
        max_length=45,
        choices=TAGS
    )

    usuario = models.ForeignKey(
        UserPetti,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.id)

    def get_image(self):
        return self.media_url.photo

    def get_user_image(self):
        return self.usuario.get_image()

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'


class Empresa(ModelBase):
    foto = models.FileField(
        upload_to='images'
    )
    nombre = models.CharField(
        max_length=45
    )
    direccion = models.CharField(
        max_length=120
    )
    telefono = models.CharField(
        max_length=45
    )
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class ServicioEmpresa(ModelBase):
    nombre = models.CharField(
        max_length=45
    )
    background = models.FileField(
        upload_to='images'
    )
    precio = models.PositiveIntegerField()
    descripcion = models.TextField(
        blank=True,
        null=True
    )
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def get_precio(self):
        return intcomma(self.precio)

    class Meta:
        verbose_name = 'Servicio empresa'
        verbose_name_plural = 'Servicios empresas'
        unique_together = [['nombre', 'empresa']]


class Reserva(ModelBase):
    usuario = models.ForeignKey(
        UserPetti,
        on_delete=models.CASCADE,
        blank=True
    )
    servicio = models.ForeignKey(
        ServicioEmpresa,
        on_delete=models.CASCADE,
    )
    estado = models.CharField(
        max_length=45,
        choices=STATUS,
        default='pendiente'
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
