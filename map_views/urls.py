from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MapViewViewSet

router = DefaultRouter()
router.register('', MapViewViewSet, basename='mapview')

urlpatterns = [
    path('', include(router.urls)),
]
