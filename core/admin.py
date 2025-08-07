from django.contrib import admin

from django.contrib import admin
from messaging.models import Message, MessageGroup
from notifications.models import Notification
from .models import User, Role , ModulePermission, FormationProcedure
from vehicles.models import Vehicle


admin.site.register(Vehicle)
admin.site.register(ModulePermission)
admin.site.register(Notification)
admin.site.register(MessageGroup)
admin.site.register(Message)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(FormationProcedure)