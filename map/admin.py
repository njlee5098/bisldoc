from django.contrib import admin

# Register your models here.

from .models import Hospital, Device


class HospitalAdmin(admin.ModelAdmin):
    search_fields = ['hospital_name']


class DeviceAdmin(admin.ModelAdmin):
    search_fields = ['hospital_name']


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Device, DeviceAdmin)
