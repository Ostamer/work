from django.contrib import admin
from .models import Settings

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'contact_email', 'contact_phone_number', 'contact_whatsapp',
        'contact_telegram', 'work_schedule', 'address', 'latitude', 'longitude'
    )
    search_fields = ('contact_email', 'contact_phone_number', 'contact_whatsapp', 'contact_telegram', 'address')
