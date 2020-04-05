from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from backend.apps.utils.shortcuts import get_object_or_none
from . import models, serializers


class TipoNecesidadViewSet(viewsets.ModelViewSet):
    queryset = models.TipoNecesidad.objects.all()
    serializer_class = serializers.TipoNecesidadSerializer
    model = models.TipoNecesidad


class ReporteNecesidadViewSet(viewsets.ModelViewSet):
    queryset = models.ReporteNecesidad.objects.all()
    serializer_class = serializers.ReporteNecesidadSerializer
    model = models.ReporteNecesidad


class UbicacionesNecesidadViewSet(viewsets.ModelViewSet):
    queryset = models.UbicacionesNecesidad.objects.all()
    serializer_class = serializers.UbicacionesNecesidadSerializer
    model = models.UbicacionesNecesidad
