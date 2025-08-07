from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, RoleViewSet,
    ModulePermissionViewSet,
    RegisterAPIView, LoginAPIView,
    FormationProcedureViewSet
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', ModulePermissionViewSet)
router.register(r'formation-procedures', FormationProcedureViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
