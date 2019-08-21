# import sys, time, curses, os, signal, psutil
# from .args import ArgsFile
# from .monitor import monitor

# music_home  = os.environ['HOME'] + '/.spools/music/'
# runner_file = 'runner'
# cmds_file   = 'cmds'

# def runner(perms, data):
# 	signal.signal(signal.SIGUSR1, parseargs)
# 	signal.signal(signal.SIGUSR2, unpause)

# 	runnerpid = get_runner_pid()

# 	while os.getpid() == runnerpid:
# 		signal.pause()


# def get_runner_pid():
# 	path = music_home + runner_file
# 	if not os.path.exists(path):
# 		return -1
# 	file = open(path, 'r')
# 	result = file.read()
# 	file.close()
# 	return int(result)

# def is_runner():
# 	pid = os.getpid()
# 	runner = get_runner_pid()

# 	return pid == runner

# def does_runner_exist():
# 	pid = get_runner_pid()
# 	try:
# 		os.kill(pid, 0)
# 		runner_create_time = psutil.Process(pid)._create_time
# 	except:
# 		return False
# 	return True

# def set_runner_pid(pid):
# 	path = music_home + runner_file
# 	file = open(path, 'w')
# 	file.write(str(pid))
# 	file.close()

# def is_runner_child():






# def create_runner(perms, data):
# 	if os.fork() > 0:
# 		sys.exit()
# 	elif os.fork() > 0:
# 		sys.exit()
# 	set_runner_pid(os.getpid())
# 	runner(perms, data)