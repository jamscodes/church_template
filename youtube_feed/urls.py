from django.urls import path
from .views import view_one_playlist, view_all_playlists

urlpatterns = [
    path("youtube_feed/", view_all_playlists, name="all_playlists"),
    path("youtube_feed/<int:playlist_id>/", view_one_playlist, name="one_playlist")
]