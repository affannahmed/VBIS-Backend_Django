from django.shortcuts import render

from rest_framework import viewsets
from .models import (
    ArtilleryReport, ContactReport, AFVStateReport,
    AmmoStateReport, FuelStateReport
)
from .serializers import (
    ArtilleryReportSerializer, ContactReportSerializer,
    AFVStateReportSerializer, AmmoStateReportSerializer,
    FuelStateReportSerializer
)

class ArtilleryReportViewSet(viewsets.ModelViewSet):
    queryset = ArtilleryReport.objects.all()
    serializer_class = ArtilleryReportSerializer

class ContactReportViewSet(viewsets.ModelViewSet):
    queryset = ContactReport.objects.all()
    serializer_class = ContactReportSerializer

class AFVStateReportViewSet(viewsets.ModelViewSet):
    queryset = AFVStateReport.objects.all()
    serializer_class = AFVStateReportSerializer

class AmmoStateReportViewSet(viewsets.ModelViewSet):
    queryset = AmmoStateReport.objects.all()
    serializer_class = AmmoStateReportSerializer

class FuelStateReportViewSet(viewsets.ModelViewSet):
    queryset = FuelStateReport.objects.all()
    serializer_class = FuelStateReportSerializer

