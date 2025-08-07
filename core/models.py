import uuid
from django.db import models


class Role(models.Model):  # Renamed from Unit
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.role_name


class ModulePermission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='permissions')
    module_name = models.CharField(max_length=100)
    full_access = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    restricted = models.BooleanField(default=False)

    class Meta:
        db_table = 'module_permissions'
        unique_together = ('role', 'module_name')

    def __str__(self):
        return f"{self.role.role_name} - {self.module_name}"


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nickname = models.CharField(max_length=100, unique=True)
    password = models.TextField()
    rank = models.CharField(max_length=50, null=True, blank=True)
    regiment = models.CharField(max_length=50, null=True, blank=True)
    vehicle_id = models.CharField(max_length=50, null=True, blank=True)
    vehicle_type = models.CharField(max_length=50, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)  # Renamed
    country = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nickname

class FormationProcedure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.code})" if self.code else self.name