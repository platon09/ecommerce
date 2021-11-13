from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from market.views.category_view import CategoryViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
       title="Market API",
       default_version='v1',
       description="""
       Documentation `Redoc` view can be found [here](/doc)
       """,
       contact=openapi.Contact(email="mukhkhamedali.muratkhan@gmail.com"),
       license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register('category', CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include([
        path('generic/', include(router.urls)),
        path('market/', include('market.urls'))
    ])),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
