from django.db import models

import uuid
from django.db import models
from core.models import User

class ArtilleryReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    time = models.TimeField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    grid_reference = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    bearing = models.CharField(max_length=20)
    action_requested = models.TextField()
    time_for_action = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)

class ContactReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report_time = models.DateTimeField()
    grid_reference = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    enemy_type = models.CharField(max_length=50)
    enemy_description = models.TextField()
    suggested_action = models.TextField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

class AFVStateReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report_type = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)
    total_vehicles = models.IntegerField()
    hit = models.IntegerField()
    balance = models.IntegerField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class AmmoStateReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ammo_type = models.CharField(max_length=50)
    total = models.IntegerField()
    consumed = models.IntegerField()
    balance = models.IntegerField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class FuelStateReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total = models.IntegerField()
    consumed = models.IntegerField()
    balance = models.IntegerField()
    mpg = models.DecimalField(max_digits=5, decimal_places=2)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
