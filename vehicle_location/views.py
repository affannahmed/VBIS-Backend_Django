from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleLocation
from .serializers import VehicleLocationSerializer

class VehicleLocationViewSet(viewsets.ModelViewSet):
    queryset = VehicleLocation.objects.all()
    serializer_class = VehicleLocationSerializer
