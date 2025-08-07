from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from core.models import User
from .models import DestructLog
from .serializers import DestructLogSerializer
from rest_framework import viewsets 

class SelfDestructAPIView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            log = DestructLog.objects.create(
                initiated_by=user,
                target_vehicle_id=user.vehicle_id,
                method='self',
                verified=True  
            )
            return Response({"message": "Self destruct initiated.", "log_id": str(log.id)}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class RemoteDestructAPIView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        password = request.data.get('password')
        target_vehicle_id = request.data.get('target_vehicle_id')

        try:
            user = User.objects.get(id=user_id)
            if not check_password(password, user.password):
                return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

            log = DestructLog.objects.create(
                initiated_by=user,
                target_vehicle_id=target_vehicle_id,
                method='remote',
                verified=True
            )
            return Response({"message": "Remote destruct initiated.", "log_id": str(log.id)}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class DestructLogViewSet(viewsets.ModelViewSet):
    queryset = DestructLog.objects.all().order_by('-created_at')
    serializer_class = DestructLogSerializer