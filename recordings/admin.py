from django.contrib import admin
from .models import Recording, RecordingShare

admin.site.register(RecordingShare)
admin.site.register(Recording)
# Register your models here.
