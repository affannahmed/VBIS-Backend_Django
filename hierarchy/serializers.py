from rest_framework import serializers
from .models import Regiment, AOR, HierarchyNode

class RegimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiment
        fields = '__all__'

class AORSerializer(serializers.ModelSerializer):
    class Meta:
        model = AOR
        fields = '__all__'

class HierarchyNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HierarchyNode
        fields = '__all__'
