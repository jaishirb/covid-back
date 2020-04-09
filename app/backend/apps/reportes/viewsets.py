from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from backend.apps.utils.shortcuts import get_object_or_none
from . import models, serializers
from ..usuarios.models import UsuarioCovid


class TipoNecesidadViewSet(viewsets.ModelViewSet):
    queryset = models.TipoNecesidad.objects.all()
    serializer_class = serializers.TipoNecesidadSerializer
    model = models.TipoNecesidad


class ReporteNecesidadViewSet(viewsets.ModelViewSet):
    queryset = models.ReporteNecesidad.objects.all()
    serializer_class = serializers.ReporteNecesidadSerializer
    model = models.ReporteNecesidad

    @action(detail=True, methods=['get'])
    def cambiar_estado(self, request, pk=None):
        estado = self.request.query_params.get('estado', None)
        reporte = get_object_or_none(self.model, id=pk)
        if estado and reporte:
            if estado == 'Activo' or estado == 'En proceso' or estado == 'Resuelto':
                reporte.estado = estado
                reporte.save()
                return Response({'status': 'success'}, status=status.HTTP_200_OK)
        return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_reportes_usuario(self, request):
        email_usuario = self.request.user.email
        usuario = get_object_or_none(UsuarioCovid, email=email_usuario)
        if usuario:
            reportes = self.model.objects.filter(usuario=usuario).exclude(estado='Resuelto')
            serializer = self.serializer_class(reportes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)


class UbicacionesNecesidadViewSet(viewsets.ModelViewSet):
    queryset = models.UbicacionesNecesidad.objects.all()
    serializer_class = serializers.UbicacionesNecesidadSerializer
    model = models.UbicacionesNecesidad
