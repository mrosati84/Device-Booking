from django.contrib import admin
from .models import Device, User

# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'serial_number', 'reserved_by']

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']

admin.site.register(Device, DeviceAdmin)
admin.site.register(User, UserAdmin)
