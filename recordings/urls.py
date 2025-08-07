from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecordingViewSet, RecordingShareViewSet

router = DefaultRouter()
router.register(r'recordings', RecordingViewSet)
router.register(r'shares', RecordingShareViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
