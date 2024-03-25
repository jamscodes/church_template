import requests as api
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.conf import settings
from .models import Playlist

BASE_URL = 'https://www.googleapis.com/youtube/v3'

# Create your views here.
## HELPER METHODS
def get_json_response(id:str) -> list:
    r = api.get(f'{BASE_URL}/playlistItems?part=snippet&playlistId={id}&key={settings.YOUTUBE_API_KEY}')
    json = r.json()

    return json['items']


## VIEW METHODS
def view_all_playlists(request):
    playlists = Playlist.objects.all().order_by('-id')[:10:-1]

    context = {
        'playlists': []
    }

    for playlist in playlists:

        if playlist.featured:
            context['featured'] = {
                'playlist': playlist,
                'videos': get_json_response(playlist.retrieve_playlist_id())
            }
        else:
            context['playlists'].append(playlist)

    return render(request, 'youtube_feed.html', context=context)


def view_one_playlist(request, playlist_id = None):
    playlist = get_object_or_404(Playlist, id=playlist_id)

    items = get_json_response(playlist.retrieve_playlist_id())

    return render(request, 'single_playlist.html', context={'playlist': playlist, 'videos': items})