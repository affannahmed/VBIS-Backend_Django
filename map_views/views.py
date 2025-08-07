from rest_framework import viewsets
from .models import MapView
from .serializers import MapViewSerializer

class MapViewViewSet(viewsets.ModelViewSet):
    queryset = MapView.objects.all()
    serializer_class = MapViewSerializer
