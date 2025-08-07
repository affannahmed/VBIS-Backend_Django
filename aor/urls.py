from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AORViewSet, AORAssignmentViewSet

router = DefaultRouter()
router.register(r'aors', AORViewSet)
router.register(r'aor-assignments', AORAssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
