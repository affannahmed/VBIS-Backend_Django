from rest_framework import viewsets, status
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.hashers import check_password
from .models import User, Role, ModulePermission , FormationProcedure
from .serializers import (
    UserSerializer, RoleSerializer,
    RegisterSerializer, LoginSerializer,
    ModulePermissionSerializer, FormationProcedureSerializer
)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class ModulePermissionViewSet(viewsets.ModelViewSet):
    queryset = ModulePermission.objects.all()
    serializer_class = ModulePermissionSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            nickname = serializer.validated_data['nickname']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(nickname=nickname)
                if check_password(password, user.password):
                    role_name = user.role.role_name if user.role else None
                    return Response({
                        "message": "Login successful",
                        "nickname": user.nickname,
                        "rank": user.rank,
                        "role_name": role_name
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class FormationProcedureViewSet(viewsets.ModelViewSet):
    queryset = FormationProcedure.objects.all()
    serializer_class = FormationProcedureSerializer