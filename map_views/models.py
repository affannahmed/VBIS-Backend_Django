from django.db import models
import uuid
from core.models import User

class MapView(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    military_symbol = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True)
    map_config = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
