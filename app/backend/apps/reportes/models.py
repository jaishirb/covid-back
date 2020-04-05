from django.contrib.gis.db import models

from backend.apps.usuarios.models import UsuarioCovid
from backend.apps.utils.constants import TIPO_PERSONA, ESTADOS_REPORTES
from backend.apps.utils.models import ModelBase


class TipoNecesidad(ModelBase):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = 'Necesidad'
        verbose_name_plural = 'Necesidades'


class ReporteNecesidad(ModelBase):
    descripcion = models.TextField(
        blank=True,
        null=True
    )
    nombre = models.CharField(max_length=45)
    edad = models.PositiveIntegerField()
    telefono = models.CharField(max_length=12)
    tipo_persona = models.CharField(
        max_length=24,
        choices=TIPO_PERSONA
    )
    tipo_necesidad = models.ForeignKey(
        TipoNecesidad,
        on_delete=models.CASCADE
    )
    usuario = models.ForeignKey(
        UsuarioCovid,
        on_delete=models.CASCADE
    )
    estado = models.CharField(
        max_length=45,
        choices=ESTADOS_REPORTES,
        default='Activo'
    )

    def __str__(self):
        return str(self.id)

    def get_ubicaciones(self):
        data = UbicacionesNecesidad.objects.filter(
            reporte_necesidad=self
        )
        from backend.apps.reportes.serializers import UbicacionesNecesidadSerializer
        return UbicacionesNecesidadSerializer(data, many=True).data

    class Meta:
        verbose_name = 'Reporte necesidad'
        verbose_name_plural = 'Reporte necesidades'


class UbicacionesNecesidad(ModelBase):
    fecha = models.DateField()
    direccion = models.CharField(max_length=120)
    ubicacion = models.PointField(blank=True, null=True)
    reporte_necesidad = models.ForeignKey(
        ReporteNecesidad,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.direccion

    class Meta:
        verbose_name = 'Ubicacion necesidad'
        verbose_name_plural = 'Ubicaciones necesidades'
