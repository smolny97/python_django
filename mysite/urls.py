from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from main.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'main',GamesViewSet)
router2 = routers.DefaultRouter()
router2.register(r'main',GameViewSet)
router3 = routers.DefaultRouter()
router3.register(r'main',BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router2.urls)),
    path('api/v1/', include(router3.urls)),
    path('', include('main.urls')),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
