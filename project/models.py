from django.db import models
from django.apps import apps

class Project(models.Model):
    # Ленивый импорт модели Client
    def get_client_model(self):
        return apps.get_model('client', 'Client')

    # Ленивый импорт модели Service
    def get_service_model(self):
        return apps.get_model('service', 'Service')

    title = models.CharField(max_length=255)
    description = models.TextField()
    area = models.FloatField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)
    duration = models.DateField(null=True, blank=True)
    # Используем строки для указания моделей
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    service = models.ForeignKey('service.Service', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'
