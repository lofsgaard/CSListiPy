from spotify import get_spotify_user, auth, create_playlist, get_spotify_tracks, add_tracks_playlist
from setlist import get_setlist

# Set auth scope, depends on what you want to do
scope = 'playlist-modify-public, playlist-modify-private, playlist-read-private'

p_name = 'Test Playlist'
p_desc = 'Test Playlist description'
setlist = '7bbc86fc'

# Runs an API call to setlist api using function get_setlist()
artist, tracks = get_setlist(setlist)

# Creates a playlist using the function create_playlist(). Parameters using the above variables
playlist = create_playlist(get_spotify_user(auth(scope)), p_name, p_desc, auth(scope))
# Gets the playlist_id from the above created playlist. Used to add songs to that playlist.
playlist_id = playlist['id']

# Runs an API call to the Spotify API using the function get_spotify_tracks(),
# using values from the setlist variable above
spotify_tracks = get_spotify_tracks(auth(scope), tracks, artist)

# Runs an API call to the Spotify using the function add_tracks_playlist()
# to add tracks from the above variable to the playlist
add_tracks_playlist(auth(scope), playlist_id, spotify_tracks)



