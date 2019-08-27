import os
class Terminal(object):
	def __init__(self, bash_profile):
		bash_profile.save()

	def run_cmd(cmd):
		os.system(cmd)