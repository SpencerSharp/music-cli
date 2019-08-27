import spotipy, spotipy.util as util

client_key = 'b4847d3dd2464848bc7f1f34b04f9509'
secret_key = '1ebd017edc044803906b36e81bd48cc3'
url        = 'http://localhost:8888/callback/'

username   = 'sharpieman20'
scopes     = [
'user-top-read',
'user-read-recently-played',
'user-read-playback-state',
'user-read-currently-playing',
'user-modify-playback-state',
'user-library-modify',
'user-library-read',
'streaming',
'app-remote-control',
'user-read-private',
'user-read-email',
'user-follow-modify',
'user-follow-read',
'playlist-modify-public',
'playlist-read-collaborative',
'playlist-read-private',
'playlist-modify-private']
scope = ' '.join(scopes)

# TODO: Replace spotipy's authentication process with your own
def get_spotify_permissions():
    token = util.prompt_for_user_token(username,scope,client_id=client_key,client_secret=secret_key,redirect_uri=url)
    global spotify
    spotify = spotipy.Spotify(auth=token)

def get_track(id):
    return spotify.track(id)

def get_track_named(name):
    val = spotify.search('tracks: ' + name, limit=1,type='track')
    val = val['tracks']['items']
    if len(val) == 0:
        return None
    return val[0]

def current_track():
    track = spotify.currently_playing()
    if track == None:
        return track
    return track['item']

def pause_player():
    spotify.pause_playback()

def unpause_player():
    spotify.start_playback()