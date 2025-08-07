from django.shortcuts import render

from rest_framework import viewsets
from .models import Regiment, AOR, HierarchyNode
from .serializers import RegimentSerializer, AORSerializer, HierarchyNodeSerializer

class RegimentViewSet(viewsets.ModelViewSet):
    queryset = Regiment.objects.all()
    serializer_class = RegimentSerializer

class AORViewSet(viewsets.ModelViewSet):
    queryset = AOR.objects.all()
    serializer_class = AORSerializer

class HierarchyNodeViewSet(viewsets.ModelViewSet):
    queryset = HierarchyNode.objects.all()
    serializer_class = HierarchyNodeSerializer

