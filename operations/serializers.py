from rest_framework import serializers
from .models import DestructLog

class DestructLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestructLog
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'verified']
