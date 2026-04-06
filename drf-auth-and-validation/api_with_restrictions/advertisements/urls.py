from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AdvertisementViewSet

router_v1 = DefaultRouter()
router_v1.register(r'', AdvertisementViewSet, basename='advertisements')

urlpatterns = [
    path('', include(router_v1.urls)),
]
