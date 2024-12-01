from django.db import models

class Employee(models.Model):
    photo_url = models.URLField(null=True, blank=True)
    full_name = models.CharField(max_length=255)
    employee_position = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'employee'