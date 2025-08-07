from django.contrib import admin
from .models import MapView

@admin.register(MapView)
class MapViewAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_default', 'created_by', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_default', 'created_by')
