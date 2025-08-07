import uuid
from django.db import models
from core.models import User  # assuming User model is in core
from hierarchy.models import Regiment  # assuming Regiment model is in core

class Frequency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    frequency = models.CharField(max_length=20, unique=True)
    regiment = models.ForeignKey(Regiment, on_delete=models.CASCADE)
    military_symbol = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.frequency

