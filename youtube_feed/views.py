import requests as api
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.conf import settings
from .models import Playlist

BASE_URL = 'https://www.googleapis.com/youtube/v3'

# Create your views here.
# class PlaylistSingleView(ListView):
#     template_name = "single_playlist.html"

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)

#     #     context["videos"] = []
#     #     context["playlist"] = {}

#     def get_queryset(self):
#         context = super().get_context_data()
#         context["playlist"] = get_object_or_404(Playlist, id=self.kwargs["playlist_id"])

#         r = api.get(f"{BASE_URL}/playlistItems?part=snippet&playlistId={context["playlist"].retrieve_playlist_id()}&key={settings.YOUTUBE_API_KEY}")
#         context["videos"] = r.json()

#         return context
    



def view_one_playlist(request, playlist_id = None):
    featured_playlist = get_object_or_404(Playlist, id=playlist_id)

    r = api.get(f'{BASE_URL}/playlistItems?part=snippet&playlistId={featured_playlist.retrieve_playlist_id()}&key={settings.YOUTUBE_API_KEY}')
    json = r.json()

    return render(request, 'single_playlist.html', context={'playlist': featured_playlist, 'videos': json['items']})