from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from backend.apps.utils.shortcuts import get_object_or_none
from . import models, serializers


class UsuarioCovidViewSet(viewsets.ModelViewSet):
    queryset = models.UsuarioCovid.objects.all()
    serializer_class = serializers.UserCovidSerializer
    model = models.UsuarioCovid