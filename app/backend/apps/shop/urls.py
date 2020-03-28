from django.urls import path, include
from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register(r'categorias', viewsets.CategoriaViewSet)
router.register(r'colores', viewsets.ColorViewSet)
router.register(r'pedidos_individuales', viewsets.PedidoIndividualViewSet)
router.register(r'pedidos', viewsets.PedidoViewSet)
router.register(r'inventarios', viewsets.InventarioViewSet)
router.register(r'', viewsets.ProductoViewSet)


urlpatterns = [
    path(r'', include(router.urls))
]