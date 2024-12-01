from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'client', 'service', 'area', 'budget', 'duration', 'created_at', 'updated_at')
    search_fields = ('title', 'client__name', 'service__title')
    list_filter = ('created_at', 'updated_at', 'client', 'service')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
