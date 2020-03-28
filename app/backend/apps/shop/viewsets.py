from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from backend.apps.utils.shortcuts import get_object_or_none
from . import models, serializers


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    model = models.Categoria


class ColorViewSet(viewsets.ModelViewSet):
    queryset = models.Color.objects.all()
    serializer_class = serializers.ColorSerializer
    model = models.Color


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = models.Producto.objects.all()
    serializer_class = serializers.ProductoSerializer
    model = models.Producto

    @action(detail=False, methods=['get'])
    def filter(self, request):
        producto = self.request.query_params.get('nombre', None)
        productos = self.model.objects.filter(
            nombre__icontains=producto
        ).distinct()[:15]
        serializer = self.serializer_class(productos, many=True)
        return Response(serializer.data)


class PedidoIndividualViewSet(viewsets.ModelViewSet):
    queryset = models.PedidoIndividual.objects.all()
    serializer_class = serializers.PedidoIndividualSerializer
    model = models.PedidoIndividual


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = models.Pedido.objects.all()
    serializer_class = serializers.PedidoSerializer
    model = models.Pedido


class InventarioViewSet(viewsets.ModelViewSet):
    queryset = models.Inventario.objects.all()
    serializer_class = serializers.InventarioSerializer
    model = models.Inventario