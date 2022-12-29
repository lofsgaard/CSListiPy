import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()


# Create a spotipy oauth2 object
def auth(scope):
    os.environ["SPOTIPY_CLIENT_ID"] = os.getenv('SPOTIPY_CLIENT_ID')
    os.environ["SPOTIPY_CLIENT_SECRET"] = os.getenv('SPOTIPY_CLIENT_SECRET')
    os.environ["SPOTIPY_REDIRECT_URI"] = 'http://127.0.0.1:8080'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp


# Get currently logged-in username, used to create playsists and other stuff
def get_spotify_user(sp):
    get_user = sp.current_user()
    spotify_user = get_user['id']
    return spotify_user


def create_playlist(username, p_name, p_desc, sp):
    new_playlist = sp.user_playlist_create(username, p_name, public=True, description=p_desc)
    return new_playlist


def get_spotify_tracks(sp, tracks, artist):
    new_tracks = []
    for track in tracks:
        sp_tracks = (sp.search(q=f'{track}, {artist}', type='track,artist', limit=1))
        for key in sp_tracks['tracks']['items']:
            new_tracks.append(key['uri'])
    return new_tracks


def add_tracks_playlist(sp, playlist_id, tracks):
    sp.playlist_add_items(playlist_id, tracks)
