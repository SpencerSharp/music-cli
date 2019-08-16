# See if a music process is already running
# If so, call its init method and exit
def check_already_running():
	sys.exit()

def create_runner():

def init_env():

def init():
	if not check_already_running():
		init_env()
		perms = get_spotify_permissions()
		data  = load_data()
		create_runner(perms, data)
	

	# ELSE

	# Get all spotify permissions

	# If $HOME/.music exists
		# Load in all our dataframes
	# Otherwise
		# Create $HOME/.music
		# Initialize all our dataframes

	# 

