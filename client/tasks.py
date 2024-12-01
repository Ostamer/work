# tasks.py
from celery import shared_task
from googleapiclient.discovery import build
from media.models import VideoReview
from project.models import Project
from datetime import datetime, timedelta
from django.utils import timezone

YOUTUBE_API_KEY = 'AIzaSyA-i5W0yi2pEnrIkIJlR6WFmAaiQZHWFI4'
channel_id = 'YOUR_CHANNEL_ID'

@shared_task
def fetch_youtube_videos(channel_id, project_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    published_after = (timezone.now() - timedelta(days=1)).isoformat("T") + "Z"

    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        publishedAfter=published_after,
        type='video'
    )
    response = request.execute()

    project = Project.objects.get(id=project_id)

    for item in response['items']:
        video_id = item['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        title = item['snippet']['title']
        description = item['snippet']['description']
        published_at = item['snippet']['publishedAt']

        if not VideoReview.objects.filter(url=video_url, project=project).exists():
            VideoReview.objects.create(
                project=project,
                url=video_url,
                title=title,
                description=description,
                published_at=published_at
            )
