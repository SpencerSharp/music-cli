import pandas as pd
class DataItem(object):
	child_map = {}

	def add_child(child, table_name):
		DataItem.child_map[table_name] = child

	def save_item(data, item_type, item):
		table_name = type(item).__name__.lower() + 's'
		#series = pd.Series(index=DataItem.get_fields(table_name,'internal'), data=item.get_as('array'))
		series = pd.Series(data=item.get_as('array'))
		return data[item_type + 's'].append(series, ignore_index=True)

	def create_item(type, map_type, item):
		if item != None:
			return DataItem.child_map[type + 's'](map_type, item)

	def table_names():
		return DataItem.child_map.keys()

	def get_fields(table_name, type='disk'):
		return DataItem.child_map[table_name].field_maps[type].keys()