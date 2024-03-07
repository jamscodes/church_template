import requests as api
from django.shortcuts import render

# Create your views here.
def feed(request):
    r = api.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=PLNj9g8xY-8YS6fQhdLXzV-YQlGblL5Ozo&key=AIzaSyDKMd3mDKXOO7aSReGbGpfD8jVuwODr9G8')
    json = r.json()
    return render(request, 'youtube_feed.html', context={'videos': json['items']})