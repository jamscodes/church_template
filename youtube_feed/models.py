from django.db import models
from .validators import validate_playlist_link_contains_list_id
# Create your models here.

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255, validators=[validate_playlist_link_contains_list_id])
    featured = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if self.featured:
            try:
                temp = Playlist.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Playlist.DoesNotExist:
                pass
        super(Playlist, self).save(*args, **kwargs)
    
    def retrieve_playlist_id(self) -> str:
        return self.link[self.link.find("list=") + 5:]