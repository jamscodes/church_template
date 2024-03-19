from django.test import TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse

from .models import Playlist
# Create your tests here.
class PlaylistModelTests(TestCase):
    def test_playlist_link_contains_list_id(self) -> None:
        """
        playlist URL needs to contain a URL parameter called 'list' that equals the playlist id
        """

        bad_playlist_link = "https://www.youtube.com/playlist"
        bad_playlist_instance = Playlist(link = bad_playlist_link)

        with self.assertRaises(ValidationError):
            bad_playlist_instance.full_clean()

class PlaylistIndexViewTests(TestCase):
    def test_no_playlist(self):
        """
        If there is not a valid playlist id, return 404
        """

        response = self.client.get(reverse("one-youtube-feed", kwargs={"playlist_id": 0}))
        self.assertEqual(response.status_code, 404)

    def test_one_playlist(self):
        """
        If we are loading the single_playlist view
        """

        new_playlist_link = "https://www.youtube.com/playlist?list=PLbpi6ZahtOH6sWdpcYk0hOP6wmUQGt97J"
        new_playlist = Playlist.objects.create(link = new_playlist_link, title = "Study buddies")

        response = self.client.get(reverse("one-youtube-feed", kwargs={"playlist_id": new_playlist.id}))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["playlist"], Playlist)
        self.assertContains(response, "<h1>Study buddies</h1>")