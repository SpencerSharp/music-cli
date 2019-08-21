# See if a music process is already running
# If so, call its init method and exit

import sys, os, time, signal
from .data import load_data
from .spotify import get_spotify_permissions
from .args import ArgsFile
from .file import music_home
from .monitor import does_monitor_exist, create_monitor

def init_env():
	# os.system('''trap 'val=$BASH_COMMAND && REGEX="^[0-9]{1,2}\.[0-9]$" && if [[ $val =~ $REGEX ]]; then echo $val && false; else true; fi' DEBUG''')
	if not os.path.exists(music_home):
		os.mkdir(music_home)
	global args_file
	args_file = ArgsFile()
	args_file.delete()

def init():
	init_env()
	get_spotify_permissions()
	if not does_monitor_exist():
		print('No monitor found')
		create_monitor(os.getppid())
	load_data()