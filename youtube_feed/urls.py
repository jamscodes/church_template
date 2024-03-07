from django.urls import path
from . import views

urlpatterns = [
    path('youtube_feed/', views.feed, name='youtube-feed')
]