"""
Usage:
    music rate [-dip] (-a|-s) <name>...

Options:
	-a 		Album name
	-s   	Song name
	-p  	Pause
	-d 		Use id instead of name
	-q 		Quiet
"""
import os, sys,signal
import pandas as pd
from docopt import docopt

from lib.data 		import tables
from lib.spotify 	import get, search

def rate():
	args = docopt(__doc__)
	if 		args['-a']:
		type   = 'album'
	elif 	args['-s']:
		type   = 'song'

	if      args['-d']:
		id     = args['<name>'][0]
	else:
		id    = search('album', ' '.join(args['<name>'][:-1]))

	item = get(type, id)

	score   = round(float(args['<name>'][-1:][0]),1)

	rate_item(item, type, score)

def rate_item(item, type, score):
	item.append(score)
	tables[type + 's'].loc[item[0]] = pd.Series(index=tables[type + 's'].columns, data=item)

def fantano():

	print('Did you love it, did you hate it, what would you rate it?')
	