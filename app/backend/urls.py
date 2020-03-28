from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from backend.apps.users.views import LoginView

router = DefaultRouter()

schema_view = get_swagger_view(title='Petti Api')

PREFIX_URL = settings.PREFIX_URL
urlpatterns = [
      url(r'^{}admin/'.format(PREFIX_URL), admin.site.urls),
      url(r'^{}auth/'.format(PREFIX_URL), include('rest_auth.urls')),
      url(r'^{}$'.format(PREFIX_URL), schema_view),
      url(r'^{}api/'.format(PREFIX_URL), include(router.urls)),
      url(r'^{}api/v1/mascotas/'.format(PREFIX_URL), include('backend.apps.mascotas.urls')),
      url(r'^{}api/v1/users/'.format(PREFIX_URL), LoginView.as_view(), name='rest_login'),
      url(r'^{}api/v1/profiles/'.format(PREFIX_URL), include('backend.apps.users.urls')),
      url(r'^{}api/v1/shop/'.format(PREFIX_URL), include('backend.apps.shop.urls')),
]

