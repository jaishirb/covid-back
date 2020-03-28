from django.urls import path, include
from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register(r'publicaciones', viewsets.PublicacionViewSet)
router.register(r'empresas', viewsets.EmpresaViewSet)
router.register(r'servicios', viewsets.ServicioEmpresaViewSet)
router.register(r'reservas', viewsets.ReservaViewSet)
router.register(r'imagenes', viewsets.ImagenViewSet)
router.register(r'', viewsets.MascotaViewSet)


urlpatterns = [
    path(r'', include(router.urls))
]