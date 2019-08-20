import time, os, signal
from .spotify import current_track
from .args import ArgsFile

def monitor(perms):
	if os.fork() > 0:
		return
	prev_track = None
	signal.signal(signal.SIGCHLD, wake_runner)
	while True:
		cur_track = current_track()
		if cur_track != prev_track:
			if os.fork() == 0:
				ArgsFile().write_args()
				sys.exit()
			time.sleep(0.1)

def wake_runner(a,b):
	os.kill(os.getppid(),signal.SIGUSR2)