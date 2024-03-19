from django.db import models
from .validators import validate_playlist_link_contains_list_id
# Create your models here.

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, validators=[validate_playlist_link_contains_list_id])
    featured = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"
    
    def retrieve_playlist_id(self) -> str:
        return self.link[self.link.find("list=") + 5:]