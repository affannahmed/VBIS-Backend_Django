from django.shortcuts import render

from rest_framework import viewsets
from .models import AOR, AORAssignment
from .serializers import AORSerializer, AORAssignmentSerializer

class AORViewSet(viewsets.ModelViewSet):
    queryset = AOR.objects.all().order_by('-created_at')
    serializer_class = AORSerializer

class AORAssignmentViewSet(viewsets.ModelViewSet):
    queryset = AORAssignment.objects.all().order_by('-assigned_at')
    serializer_class = AORAssignmentSerializer

