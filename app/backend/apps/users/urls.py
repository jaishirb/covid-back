from django.urls import path, include
from rest_framework import routers
from . import viewsets, views

router = routers.DefaultRouter()
router.register(r'', viewsets.UserPettiViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]