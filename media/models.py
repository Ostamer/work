from django.db import models

class Image(models.Model):
    # Просто указываем строку с именем модели
    project = models.ForeignKey('project.Project', on_delete=models.CASCADE)
    url = models.URLField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Изображения для проекта {self.project.title}"

    class Meta:
        db_table = 'image'


class VideoReview(models.Model):
    url = models.URLField()
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Видео отзывы для проекта {self.project.title}"

    class Meta:
        db_table = 'videoreviews'
