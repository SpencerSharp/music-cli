# See if a music process is already running
# If so, call its init method and exit

import sys, os, time, signal
from .data import load_data
from .spotify import get_spotify_permissions
from .args import ArgsFile
from .file import music_home

def init_env():
	if not os.path.exists(music_home):
		os.mkdir(music_home)
	global args_file
	args_file = ArgsFile()
	args_file.delete()

def init():
	#if not does_runner_exist():
	init_env()
	get_spotify_permissions()
	load_data()
		# create_runner(perms, data)
	# args_file = ArgsFile()
	# if not is_runner():
	# 	args_file.write_args(sys.argv)
	# 	os.kill(get_runner_pid(), signal.SIGUSR1)
	# 	sys.exit()
	# args_file.read_args()