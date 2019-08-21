from .remote import *
from .file import get_path
import os, pandas as pd
rel_path = 'data'
abs_path = get_path(rel_path)
global data
data = {}

def get_path(table_name):
	return abs_path + '/' + table_name

def acquire_key():
	global key
	key = open(abs_path + '.key', 'w')

def release_key():
	key.close()

def init_table(table_name):
	table = pd.DataFrame(columns=table_cols[table_name])
	tables[table_name] = table
	table.to_json(get_path(table_name))

def load_table(table_name):
	table = pd.read_json(get_path(table_name))
	table = table.set_index('id',drop=False)
	tables[table_name] = table

def create_local():
	acquire_key()
	if not os.path.exists(abs_path):
		os.mkdir(abs_path)
	for table_name in table_cols.keys():
		init_table(table_name)

def load_from_local():
	acquire_key()
	for table_name in table_cols.keys():
		load_table(table_name)

def save_to_local():
	for table_name in table_cols.keys():
		tables[table_name].to_json(get_path(table_name))
	release_key()

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
	else:
		load_from_local()