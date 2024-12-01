from django.contrib import admin
from .models import Image, VideoReview

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'description')
    search_fields = ('description',)

@admin.register(VideoReview)
class VideoReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'description')
    search_fields = ('description',)
