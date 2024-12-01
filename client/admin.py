from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'address')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('address',)
    ordering = ('id',)
