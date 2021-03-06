from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from api import urls as apiURLs
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from config import envs

schema_view = get_schema_view(
    openapi.Info(
        title="API Document",
        default_version=envs.API_VERSION,
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(apiURLs)),
    url(
        r'^swagger/(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    url(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
]