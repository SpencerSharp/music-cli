import os, signal
from lib.spotify import pause_player, unpause_player
def prompt_and_get_rating(item):
	info = open('/Users/spencersharp/.spools/music/info.txt','w')
	info.write('rate -dpq ' + item.flag() + ' ' + item.id )
	info.close()
	print('\nPlease score {}: '.format(item.name), end='', flush=True)
	pause()

def pause():
	signal.signal(signal.SIGUSR1, wake_on_signal_received)
	pause_player()
	signal.pause()
	unpause_player()
	signal.signal(signal.SIGUSR1, signal.SIG_IGN)

def send_signal(pid, sig):
	if pid > 0:
		os.kill(pid,sig)

def wake_on_signal_received(a,b):
	test = 'fool'