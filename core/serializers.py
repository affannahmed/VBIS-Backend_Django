from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Role, ModulePermission
from .models import FormationProcedure

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class ModulePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModulePermission
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'password', 'rank', 'regiment',
                  'vehicle_id', 'vehicle_type', 'role', 'country']

    def validate_password(self, value):
        return make_password(value)

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class LoginSerializer(serializers.Serializer):
    nickname = serializers.CharField()
    password = serializers.CharField()




class FormationProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormationProcedure
        fields = '__all__'