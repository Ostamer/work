from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'employee_position', 'photo_url')
    search_fields = ('full_name', 'employee_position')
