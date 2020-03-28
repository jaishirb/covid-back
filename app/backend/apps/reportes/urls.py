
from django.urls import path, include
from rest_framework import routers
from . import viewsets
 
router = routers.DefaultRouter()
router.register(r'tipos_necesidades', viewsets.TipoNecesidadViewSet)
router.register(r'reportes_covid', viewsets.ReporteCovidViewSet)
router.register(r'reportees_necesidades', viewsets.ReporteNecesidadViewSet)
router.register(r'ubicaciones_necesidades', viewsets.UbicacionesNecesidadViewSet)
router.register(r'', viewsets.UbicacionesCovidViewSet)


urlpatterns = [
    path(r'', include(router.urls))
]