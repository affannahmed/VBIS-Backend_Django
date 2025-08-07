from django.contrib import admin

# Register your models here.
from .models import Regiment, AOR, HierarchyNode

admin.site.register(Regiment)
admin.site.register(AOR)
admin.site.register(HierarchyNode)
