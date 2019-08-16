aliases     = []
queue       = []
artist_cols = ['id', 'album_ids', 'name']
album_cols  = ['id', 'song_ids', 'name', 'rating']
song_cols   = ['id', 'name', 'rating', 'genres', 'tags']
genre_cols  = ['id', 'parent_ids', 'name']
tag_cols    = ['id', 'parent_ids', 'name']

def create_local():

def load_from_local():

def load_data():
	# This should make sure our .music is either created and pushed to remote or pulled from remote
	if remote_exists():
		sync_remote()
	else:
		create_local()
		set_remote()
		push_to_remote()

	load_from_local()