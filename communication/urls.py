from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FrequencyViewSet

router = DefaultRouter()
router.register(r'frequencies', FrequencyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
