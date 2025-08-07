from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Frequency
from .serializers import FrequencySerializer

class FrequencyViewSet(viewsets.ModelViewSet):
    queryset = Frequency.objects.all().order_by('-created_at')
    serializer_class = FrequencySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

