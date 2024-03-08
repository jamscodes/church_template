import requests as api
from django.shortcuts import render
from django.conf import settings

BASE_URL = 'https://www.googleapis.com/youtube/v3'

# Create your views here.
def feed(request):
    # latest = api.get()
    print(settings.YOUTUBE_API_KEY)
    r = api.get(f'{BASE_URL}/playlistItems?part=snippet&playlistId=PLNj9g8xY-8YS6fQhdLXzV-YQlGblL5Ozo&key={settings.YOUTUBE_API_KEY}')
    json = r.json()
    print(json)
    return render(request, 'youtube_feed.html', context={'videos': json['items']})