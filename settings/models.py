from django.db import models


class Settings(models.Model):
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone_number = models.CharField(max_length=20, null=True, blank=True)
    contact_whatsapp = models.CharField(max_length=20, null=True, blank=True)
    contact_telegram = models.CharField(max_length=50, null=True, blank=True)
    work_schedule = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return "Настройки"

    class Meta:
        db_table = 'settings'