from django.contrib import admin
from .models import AOR, AORAssignment

@admin.register(AOR)
class AORAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'military_symbol', 'created_by', 'created_at')
    list_filter = ('type', 'created_at')
    search_fields = ('name', 'military_symbol', 'created_by__username')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(AORAssignment)
class AORAssignmentAdmin(admin.ModelAdmin):
    list_display = ('aor', 'assigned_to', 'assigned_at')
    list_filter = ('assigned_at',)
    search_fields = ('aor__name', 'assigned_to__username')
    readonly_fields = ('assigned_at',)
    ordering = ('-assigned_at',)

