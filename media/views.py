# # my_app/views.py
#
# from django.shortcuts import render, redirect
# from .tasks import fetch_youtube_videos
# from .models import VideoReview
# from django.contrib import messages
#
#
# def update_videos_view(request):
#     if request.method == 'POST':
#         fetch_youtube_videos.delay()  # Запуск задачи Celery
#         messages.success(request, "Видео обновляются. Подождите несколько минут.")
#         return redirect('video_review_list')
#
#     videos = VideoReview.objects.all()
#     return render(request, 'video_review_list.html', {'videos': videos})
