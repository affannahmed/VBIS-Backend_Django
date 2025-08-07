import uuid
from django.db import models
from core.models import User 

class AOR(models.Model):
    DRAW = 'draw'
    UPLOAD = 'upload'
    TYPE_CHOICES = [
        (DRAW, 'Draw'),
        (UPLOAD, 'Upload'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    military_symbol = models.CharField(max_length=50, null=True, blank=True)
    file_reference = models.TextField(null=True, blank=True)
    drawn_data = models.JSONField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AORAssignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    aor = models.ForeignKey(AOR, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AOR {self.aor.name} -> {self.assigned_to.username if self.assigned_to else 'Unassigned'}"
