"""
Usage:
    music rate [-di] (-a|-s) <name>...

Options:
	-a 		Album name
	-s   	Song name
	-d 		Use id instead of name
	-i 		Interactive
"""
import os, sys
import pandas as pd
from docopt import docopt

from lib.data 		import tables
from lib.spotify 	import search

def rate():
	args = docopt(__doc__)
	name    = ' '.join(args['<name>'][:-1])
	score   = round(float(args['<name>'][-1:][0]),1)
	gave_id = args['-d']
	if  	args['-a']:
		rate_album(name,score,gave_id)
	elif 	args['-s']:
		rate_song(name,score,gave_id)

def rate_album(album_name, score, gave_id):
	if not gave_id:
		album = search('album', album_name)
	else:
		album = get('album', album_name)
	album.append(score)
	tables['albums'].loc[album[0]] = pd.Series(index=['id', 'song_ids', 'name', 'rating'], data=album)

def rate_song(song_name, score, gave_id):
	if not gave_id:
		song = search('track',song_name)
	else:
		song = get('track', song_name)

def fantano():
	print('Did you love it, did you hate it, what would you rate it?')
	