from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from main.views import index, ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('set_language/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', index),
    path('', include(router.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)