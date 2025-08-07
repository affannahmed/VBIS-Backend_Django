from django.db import models

import uuid
from django.db import models
from core.models import Role, User  

class Regiment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AOR(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    file_reference = models.TextField(null=True, blank=True)
    military_symbol = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=[('draw', 'Draw'), ('upload', 'Upload')])
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='aors_created')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class HierarchyNode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    regiment = models.ForeignKey(Regiment, on_delete=models.CASCADE)
    node_type = models.CharField(max_length=50)  # 'CO', 'TL', etc.
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    parent_node = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    aor = models.ForeignKey(AOR, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.node_type} in {self.regiment.name}"
        
