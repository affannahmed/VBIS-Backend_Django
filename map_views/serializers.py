from rest_framework import serializers
from .models import MapView

class MapViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapView
        fields = '__all__'
