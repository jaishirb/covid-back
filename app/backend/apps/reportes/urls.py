
from django.urls import path, include
from rest_framework import routers
from . import viewsets
 
router = routers.DefaultRouter()
router.register(r'tipos_necesidades', viewsets.TipoNecesidadViewSet)
router.register(r'ubicaciones_necesidades', viewsets.UbicacionesNecesidadViewSet)
router.register(r'', viewsets.ReporteNecesidadViewSet)


urlpatterns = [
    path(r'', include(router.urls))
]