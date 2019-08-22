# See if a music process is already running
# If so, call its init method and exit

import sys, os, time, signal
from ipc.terminal import send_signal
from data import *
from .data import load_data
from .spotify import get_spotify_permissions
from filesys.args import ArgsFile
from filesys.file import music_home
from procs.monitor import does_monitor_exist, create_monitor, get_monitor_pid

def init_env():
	dynamic_rating_cmd =  '\nshopt -s extdebug'
	dynamic_rating_cmd += '''\ntrap 'val=$BASH_COMMAND && REGEX="^[0-9]{1,2}\.[0-9]$"'''
	dynamic_rating_cmd += ''' && if [[ $val =~ $REGEX ]]; then python '''
	dynamic_rating_cmd += '''/Users/spencersharp/Documents/Coding/Active/spools-music/src/music.py '''
	dynamic_rating_cmd += '''`cat $HOME/.spools/music/info.txt` $val && false; else true; '''
	dynamic_rating_cmd += '''fi' DEBUG'''
	bashrc = open(os.environ['HOME'] + '/.bashrc', 'r')
	already_saved = False
	for line in bashrc:
		if 'DEBUG' in line:
			already_saved = True
	bashrc.close()
	bashrc = open(os.environ['HOME'] + '/.bashrc', 'a')
	if not already_saved:
		bashrc.write(dynamic_rating_cmd)
	bashrc.close()
	os.system('. ~/.bashrc')

def init_files():
	if not os.path.exists(music_home):
		os.mkdir(music_home)
	if not os.path.exists(music_home + 'info.txt'):
		info = open(music_home + 'info.txt','w')
		info.write('yeehaw')
		info.close()
	if not os.path.exists(music_home + 'monitor_block'):
		info = open(music_home + 'monitor_block','w')
		info.write('get blocked noob')
		info.close()

def alert():
	if alert_pid != get_monitor_pid():
		os.waitpid(alert_pid,0)
		blocked.close()

def init():
	init_env()
	init_files()
	get_spotify_permissions()
	global alert_pid
	alert_pid = 0
	if not does_monitor_exist():
		print('Restarting spotify daemon...',flush=True)
		global blocked
		alert_pid, blocked = create_monitor()
	else:
		alert_pid = get_monitor_pid()
	load_data()