from django.test import TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.core.cache import cache

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
    
    def test_only_one_featured_playlist(self) -> None:
        """
        ensure that when a new featured playlist is created, the previously featured playlist is no longer featured
        """

        new_playlist_link = "https://www.youtube.com/playlist?list=PLbpi6ZahtOH6sWdpcYk0hOP6wmUQGt97J"
        new_playlist_one = Playlist.objects.create(link = new_playlist_link, title = "Study buddies", featured = True)
        new_playlist_one = Playlist.objects.create(link = new_playlist_link, title = "Study buddies two", featured = True)

        featured_playlists = Playlist.objects.filter(featured = True)

        self.assertEqual(len(featured_playlists), 1)


class PlaylistIndexViewTests(TestCase):
    def test_no_playlist(self):
        """
        If there is not a valid playlist id, return 404
        """

        response = self.client.get(reverse("one_playlist", kwargs={"playlist_id": 0}))
        self.assertEqual(response.status_code, 404)

    def test_one_playlist(self):
        """
        If we are loading the single_playlist view
        """

        new_playlist_link = "https://www.youtube.com/playlist?list=PLbpi6ZahtOH6sWdpcYk0hOP6wmUQGt97J"
        new_playlist = Playlist.objects.create(link = new_playlist_link, title = "Study buddies")

        response = self.client.get(reverse("one_playlist", kwargs={"playlist_id": new_playlist.id}))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["playlist"], Playlist)
        self.assertContains(response, "<h1>Study buddies</h1>")

    def test_page_caching(self):
        url = reverse('all_playlists')
        
        # Making request to the page once
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response is coming from the cache
        self.assertTrue(response['X-Cache'], 'HIT')

        # Making request to the page again
        response = self.client.get(url)
        
        # Check if the response is coming from the cache
        self.assertTrue(response['X-Cache'], 'HIT')