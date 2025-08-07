from django.db import models

import uuid
from django.db import models
from vehicles.models import Vehicle  # Make sure this path is valid

class VehicleLocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_a = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_a_interactions')
    vehicle_b = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_b_interactions')
    latitude = models.FloatField()
    longitude = models.FloatField()
    interaction_type = models.CharField(max_length=50)
    distance_meters = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.vehicle_a} ↔ {self.vehicle_b} ({self.interaction_type})"

