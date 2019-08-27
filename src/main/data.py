import os
import file
import pandas as pd
tables = {}

def set_tables(new_tables):
    global tables
    tables = new_tables

def get_table_name(item):
    if type(item) != type:
        item = type(item)
    return item.__name__.lower() + 's'

def create_table(item):
    table_name = get_table_name(item)
    tables[table_name] = pd.DataFrame()
    set_tables(tables)

def save_tables():
    for table_name, table in tables.items():
        tables[table_name].to_json(file.get_path(table_name))

def load_tables():
    to_create = []
    for table_name, table in tables.items():
        json_file = file.get_path(table_name)
        if os.path.exists(json_file):
            tables[table_name] = pd.read_json(file.get_path(table_name))
        else:
            to_create.append(table_name)
    for name in to_create:
        tables[table_name] = pd.DataFrame()
    set_tables(tables)

def save_item(item):
    table_name = get_table_name(item)
    series = item.get_as('dataframe',len(tables[table_name]))
    tables[table_name] = tables[table_name].append(series)
    set_tables(tables)

def get_fields(table_name):
    return DataItem.child_map[table_name].field_maps[type].keys()