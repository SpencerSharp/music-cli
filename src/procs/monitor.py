import time, os, sys, signal, subprocess
from .spotify import current_album_name, current_track_name, current_track_id, pause, get
from .file    import get_path
from .data 	  import load_from_local, save_to_local

def create_monitor(tid):
	# to_zap = os.fork()
	# if to_zap == 0:
	# 	# Child to get zapped
	# 	try:
	# 		time.sleep(100000)
	# 	except:
	# 		sys.exit()
	if os.fork() == 0:
		# if os.fork() > 0:
		# 	sys.exit()
		set_monitor_pid(os.getpid())
		# os.kill(to_zap, signal.SIGINT)
		monitor(tid)
	# os.waitpid(to_zap,0)

def monitor(tid):
	prev_track = None
	prev_album = None
	while True:
		cur_track = current_track_name()
		cur_album = current_album_name()
		if cur_track != prev_track:
			if prev_track != None:
				info = open('/Users/spencersharp/.spools/music/info.txt','w')
				info.write('rate -dp -s ' + current_track_id() )#+ ' | /dev/tty')
				info.close()
				print('\nPlease score {}: '.format(cur_track), end='', flush=True)
				pause()
				#os.kill(tid, signal.SIGUSR1)
				# os.open(tid)
				# #os.system(cmd)
				# os.close(tid)
				#subprocess.call(["python"],path,"rate","-dip","-s", cur_track],shell=True)
			prev_track = cur_track
		if cur_album != prev_album:
			if prev_album != None:
				cmd =  'python /Users/spencersharp/Documents/Coding/Active/spools-music/src/music.py'
				cmd += ' rate -dp -a ' + cur_album
				#subprocess.call(cmd)
			prev_album = cur_album
		time.sleep(0.1)

def get_monitor_path():
	return get_path('monitor')

def set_monitor_pid(pid):
	path = get_monitor_path()
	file = open(path, 'w')
	file.write(str(pid))
	file.close()

def get_monitor_pid():
	path = get_monitor_path()
	if not os.path.exists(path):
		return -1
	file = open(path, 'r')
	result = file.read()
	file.close()
	return int(result)

def does_monitor_exist():
	pid = get_monitor_pid()
	try:
		os.kill(pid, 0)
	except:
		return False
	return True