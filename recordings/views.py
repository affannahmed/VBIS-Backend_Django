from rest_framework import viewsets
from .models import Recording, RecordingShare
from .serializers import RecordingSerializer, RecordingShareSerializer, RecordingShareDetailSerializer

class RecordingViewSet(viewsets.ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer

class RecordingShareViewSet(viewsets.ModelViewSet):
    queryset = RecordingShare.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RecordingShareDetailSerializer
        return RecordingShareSerializer

