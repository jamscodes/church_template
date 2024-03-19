from django.urls import path
from .views import view_one_playlist

urlpatterns = [
    # path("youtube_feed/", views.feed, name="youtube-feed"),
    path("youtube_feed/<int:playlist_id>/", view_one_playlist, name="one-youtube-feed")
]