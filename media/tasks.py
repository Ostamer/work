# # my_app/tasks.py
#
# from celery import shared_task
# from .models import VideoReview
# import requests
# from django.utils import timezone
#
# YOUTUBE_API_KEY = 'AIzaSyA-i5W0yi2pEnrIkIJlR6WFmAaiQZHWFI4'
#
#
# @shared_task
# def fetch_youtube_videos():
#     channel_id = 'UCdKuE7a2QZeHPhDntXVZ91w'
#     url = f'https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=10'
#
#     response = requests.get(url)
#     print(response.status_code)
#     print("aboba")
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#         for item in data['items']:
#             video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
#             title = item['snippet']['title']
#             description = item['snippet']['description']
#             published_at = item['snippet']['publishedAt']
#
#             VideoReview.objects.update_or_create(
#                 url=video_url,
#                 defaults={
#                     'title': title,
#                     'description': description,
#                     'published_at': timezone.datetime.fromisoformat(published_at[:-1])
#                 }
#             )
