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


class ReporteCovidViewSet(viewsets.ModelViewSet):
    queryset = models.ReporteCovid.objects.all()
    serializer_class = serializers.ReporteCovidSerializer
    model = models.ReporteCovid


class UbicacionesCovidViewSet(viewsets.ModelViewSet):
    queryset = models.UbicacionesCovid.objects.all()
    serializer_class = serializers.UbicacionesCovidSerializer
    model = models.UbicacionesCovid


class ReporteNecesidadViewSet(viewsets.ModelViewSet):
    queryset = models.ReporteNecesidad.objects.all()
    serializer_class = serializers.ReporteNecesidadSerializer
    model = models.ReporteNecesidad


class UbicacionesNecesidadViewSet(viewsets.ModelViewSet):
    queryset = models.UbicacionesNecesidad.objects.all()
    serializer_class = serializers.UbicacionesNecesidadSerializer
    model = models.UbicacionesNecesidad
