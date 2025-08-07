from django.contrib import admin
from .models import (
    ArtilleryReport, ContactReport, AFVStateReport,
    AmmoStateReport, FuelStateReport
)

@admin.register(ArtilleryReport)
class ArtilleryReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'reported_by', 'grid_reference')
    search_fields = ('grid_reference', 'reported_by__username')
    list_filter = ('date',)

@admin.register(ContactReport)
class ContactReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_time', 'grid_reference', 'latitude', 'longitude')
    search_fields = ('grid_reference',)
    list_filter = ('report_time',)

@admin.register(AFVStateReport)
class AFVStateReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_type', 'vehicle_type', 'total_vehicles', 'hit', 'balance', 'reported_by', 'created_at')
    search_fields = ('vehicle_type',)
    list_filter = ('report_type', 'vehicle_type', 'created_at')

@admin.register(AmmoStateReport)
class AmmoStateReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'ammo_type', 'total', 'consumed', 'balance', 'reported_by', 'created_at')
    search_fields = ('ammo_type',)
    list_filter = ('ammo_type', 'created_at')

@admin.register(FuelStateReport)
class FuelStateReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'consumed', 'balance', 'mpg', 'reported_by', 'created_at')
    search_fields = ('reported_by__username',)
    list_filter = ('created_at',)
