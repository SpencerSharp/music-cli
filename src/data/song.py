def Song(object):
	id          = ''
	name        = ''
	user_rating = np.nan
	log_ids     = []

	# Redundant but helpful - If we make a runner, don't save this data, just construct it on init
	# References
	artist_id   = ''
	secondary_artist_ids = []
	genre_ids = []
	tag_ids = []

	# Aggregate stats
	adjusted_score  = np.nan
	predicted_score = np.nan