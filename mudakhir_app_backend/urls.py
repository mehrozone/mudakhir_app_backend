from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Mudakhir API",
      default_version='v0',
      description="API documentation for Mudakhir App",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@mudakhir.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v0/', include('user.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "Admin"
admin.site.site_title = "Portal"
admin.site.index_title = "Welcome to Admin Portal"
