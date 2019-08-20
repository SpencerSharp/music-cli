from .remote import *
from .file import File
import os, pandas as pd
table_cols = {
	'aliases': ['id', 'name', 'action'],
	'queue'  : ['id'],
	'artists': ['id', 'album_ids', 'name'],
	'albums' : ['id', 'song_ids', 'name', 'rating'],
	'songs'  : ['id', 'name', 'rating', 'genres', 'tags'],
	'genres' : ['id', 'parent_ids', 'name'],
	'tags'   : ['id', 'parent_ids', 'name'],
}
rel_path = 'data/'
abs_path = File.get_path(rel_path)
global tables
tables = {}

def get_path(table_name):
	return abs_path + table_name

def init_table(table_name):
	table = pd.DataFrame(columns=table_cols[table_name]).to_json(get_path(table_name))

def load_table(table_name):
	table = pd.read_json(get_path(table_name))
	table = table.set_index('id',drop=False)
	tables[table_name] = table

def create_local():
	if not os.path.exists(abs_path):
		os.mkdir(abs_path)
	for table_name in table_cols.keys():
		init_table(table_name)

def save_to_local():
	for table_name in table_cols.keys():
		tables[table_name].to_json(get_path(table_name))

def load_from_local():
	for table_name in table_cols.keys():
		load_table(table_name)

def local_exists():
	return os.path.exists(abs_path)

def load_data():
	# This should make sure our .music is either created and pushed to remote or pulled from remote
	if remote_exists():
		sync_remote()
	elif not local_exists():
		create_local()
		set_remote()
		push_to_remote()

	load_from_local()