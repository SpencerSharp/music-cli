import os, signal, sys
import webbrowser
import requests
import ipc

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

def create_tcpserver(to_kill):
    import http.server
    import socketserver

    PORT = 8888
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        ipc.send_signal(to_kill, signal.SIGUSR1)
        req = httpd.handle_request()
        print('reqd')
        print(req)
        print('reqd')

# TODO: Replace spotipy's authentication process with your own
def get_token():
    params = {
        'client_id': client_key,
        'response_type': 'code',
        'redirect_uri': url,
        'scope': scope,
        'show_dialog': False
    }
    token = requests.get('https://accounts.spotify.com/authorize',params=params)
    to_access = token.url

    to_kill = os.fork()
    if to_kill == 0:
        print('wtfsir')
        signal.pause()
        sys.exit()
    if os.fork() == 0:
        create_tcpserver(to_kill)
        sys.exit()
    try:
        os.waitpid(to_kill, 0)
    except:
        print('wait not good')

    callback = webbrowser.open(to_access)
    print('------')
    print(callback.url)
    print('------')
    return token

def get_track(id):
    return spotify.track(id)

def get_track_named(name):
    val = spotify.search('tracks: ' + name, limit=1,type='track')
    val = val['tracks']['items']
    if len(val) == 0:
        return None
    return val[0]

def current_track():
    result = requests.get('https://api.spotify.com/v1/me/player/currently-playing')
    print('wtfland')
    print(result)
    print('wtfland')
    track = spotify.current_user_playing_track()
    if track == None:
        return track
    return track['item']

def pause_player():
    spotify.pause_playback()

def unpause_player():
    spotify.start_playback()