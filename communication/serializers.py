from rest_framework import serializers
from .models import Frequency

class FrequencySerializer(serializers.ModelSerializer):
    regiment_name = serializers.CharField(source='regiment.name', read_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Frequency
        fields = ['id', 'frequency', 'military_symbol', 'regiment', 'regiment_name', 'created_by', 'created_by_username', 'created_at']
