from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import AllowAny
from backend.apps.utils.print_colors import _green
from backend.apps.utils.shortcuts import get_object_or_none
from . import models, serializers


class UserPettiViewSet(viewsets.ModelViewSet):
    queryset = models.UserPetti.objects.all()
    serializer_class = serializers.UserPettiSerializer
    model = models.UserPetti

    @action(detail=False, methods=['get'])
    def get_profile(self, request):
        user_id = request.user.email
        profile = get_object_or_none(models.UserPetti, email=user_id)
        serializer = serializers.UserPettiSerializer(profile)
        data = {'id': profile.id}
        for key in serializer.data.keys():
            data[key] =  serializer.data[key]
        return Response(data, status=status.HTTP_200_OK)

