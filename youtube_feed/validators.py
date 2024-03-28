from django.core.exceptions import ValidationError

def validate_playlist_link_contains_list_id(playlistLink:str) -> bool:
    if "list=" not in playlistLink:
        raise ValidationError(f"{playlistLink} does not have a a 'list' parameter in it.\nPlease copy the entire playlist link from YouTube.")