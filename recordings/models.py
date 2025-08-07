import uuid
from django.db import models
from core.models import User  

class Recording(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.CharField(max_length=100)
    mission_name = models.CharField(max_length=100, null=True, blank=True)
    military_symbol = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='recordings')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

class RecordingShare(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recording = models.ForeignKey(Recording, on_delete=models.CASCADE, related_name='shares')
    shared_with_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_recordings')
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recording.file_name} -> {self.shared_with_user.nickname}"
