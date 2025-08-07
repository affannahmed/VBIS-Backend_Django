from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SelfDestructAPIView, RemoteDestructAPIView, DestructLogViewSet  # Don't forget to import ViewSet

router = DefaultRouter()
router.register('logs', DestructLogViewSet, basename='destructlog')

urlpatterns = [
    path('self-destruct/', SelfDestructAPIView.as_view(), name='self-destruct'),
    path('remote-destruct/', RemoteDestructAPIView.as_view(), name='remote-destruct'),
    path('', include(router.urls)), 
]
