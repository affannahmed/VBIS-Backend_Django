from django.db import models

import uuid
from django.db import models

class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_id = models.CharField(max_length=50, unique=True)
    vehicle_type = models.CharField(max_length=50)
    regiment = models.CharField(max_length=50)
    military_symbol = models.CharField(max_length=50)
    #assigned_user = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_id

