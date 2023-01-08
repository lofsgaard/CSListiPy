from spotify import get_spotify_user, auth, create_playlist, get_spotify_tracks, add_tracks_playlist
from setlist import get_setlist
import logging
from pyfiglet import Figlet


f = Figlet(font='standard')

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')


# Set auth scope, depends on what you want to do
scope = 'playlist-modify-public, playlist-modify-private, playlist-read-private'

print(f.renderText('CSListiPy'))

setlist = input("SetlistID from setlist.fm: ")

# Runs an API call to setlist api using function get_setlist()
artist, tracks, venue, city, country = get_setlist(setlist)
print(f.renderText(f'{artist}'))
logging.info('Tracks, artist and other relevant info fetched from Setlist')
p_name = f'{artist} at {venue} in {city}, {country}'
p_desc = f'Live setlist with {artist}'

# Creates a playlist using the function create_playlist(). Parameters using the above variables
playlist = create_playlist(get_spotify_user(auth(scope)), p_name, p_desc, auth(scope))
# Gets the playlist_id from the above created playlist. Used to add songs to that playlist.
playlist_id = playlist['id']
logging.info('Playlist created')

# Runs an API call to the Spotify API using the function get_spotify_tracks(),
# using values from the setlist variable above
spotify_tracks = get_spotify_tracks(auth(scope), tracks, artist)
logging.info('Tracks fetched from Spotify API')

# Runs an API call to the Spotify using the function add_tracks_playlist()
# to add tracks from the above variable to the playlist
add_tracks_playlist(auth(scope), playlist_id, spotify_tracks)
logging.info('Tracks added from setlist to playlist!')
