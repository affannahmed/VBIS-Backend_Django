from rest_framework import serializers
from .models import (
    ArtilleryReport, ContactReport, AFVStateReport,
    AmmoStateReport, FuelStateReport
)

class ArtilleryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtilleryReport
        fields = '__all__'

class ContactReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactReport
        fields = '__all__'

class AFVStateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AFVStateReport
        fields = '__all__'

class AmmoStateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmmoStateReport
        fields = '__all__'

class FuelStateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelStateReport
        fields = '__all__'
