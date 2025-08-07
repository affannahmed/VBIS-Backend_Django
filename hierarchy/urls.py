from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegimentViewSet, AORViewSet, HierarchyNodeViewSet

router = DefaultRouter()
router.register(r'regiments', RegimentViewSet)
router.register(r'aors', AORViewSet)
router.register(r'hierarchy-nodes', HierarchyNodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
