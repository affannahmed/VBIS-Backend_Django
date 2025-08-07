from rest_framework import serializers
from .models import AOR, AORAssignment

class AORSerializer(serializers.ModelSerializer):
    class Meta:
        model = AOR
        fields = '__all__'

class AORAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AORAssignment
        fields = '__all__'
