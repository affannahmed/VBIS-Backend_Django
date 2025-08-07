from django.db import models

import uuid
from django.db import models
from core.models import User

class DestructLog(models.Model):
    METHOD_CHOICES = [
        ('self', 'Self Destruct'),
        ('remote', 'Remote Destruct'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    initiated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    target_vehicle_id = models.CharField(max_length=50)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method.upper()} destruct by {self.initiated_by.nickname}"

