from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from backend.apps.utils.shortcuts import get_object_or_none
from . import models, serializers


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = models.Mascota.objects.all()
    serializer_class = serializers.MascotaSerializer
    model = models.Mascota


class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = models.Publicacion.objects.all()
    serializer_class = serializers.PublicacionSerializer
    model = models.Publicacion

    @action(detail=True, methods=['post'])
    def update_likes(self, request, pk=None):
        publicacion = models.Publicacion.objects.get(pk=pk)
        for like in request.data.keys():
            publicacion.likes[like] = request.data[like]
            publicacion.save()
        return Response({'status': 'success'}, status=status.HTTP_200_OK)

    def get_queryset(self):
        action_method = self.request.query_params.get('action')
        if action_method == 'adopcion':
            return self.model.objects.filter(archived=False, tag='adopcion').order_by('-id')
        elif action_method == 'compraventa':
            return self.model.objects.filter(archived=False, tag='compraventa').order_by('-id')
        elif action_method == 'parejas':
            return self.model.objects.filter(archived=False, tag='parejas').order_by('-id')
        else:
            return self.model.objects.all().order_by('-id')


class ImagenViewSet(viewsets.ModelViewSet):
    queryset = models.Imagen.objects.all()
    serializer_class = serializers.ImagenSerializer
    model = models.Imagen
    parser_classes = [MultiPartParser, FormParser]


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = models.Empresa.objects.all()
    serializer_class = serializers.EmpresaSerializer
    model = models.Empresa


class ServicioEmpresaViewSet(viewsets.ModelViewSet):
    queryset = models.ServicioEmpresa.objects.all()
    serializer_class = serializers.ServicioEmpresaSerializer
    model = models.ServicioEmpresa


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = models.Reserva.objects.all()
    serializer_class = serializers.ReservaSerializer
    model = models.Reserva
