import sqlite3
import os

class Table():
    APPLICATION_FOLDER = 'app'
    DATABASES_FOLDER = os.path.join(APPLICATION_FOLDER, 'databases')
    BACKUP_SCHEMAS_FOLDER = os.path.join(DATABASES_FOLDER, 'backup_schemas')
    SENSOR_DATA_TABLE_CREATION_QUERY = os.path.join(BACKUP_SCHEMAS_FOLDER, 'sensor_data_table_creation_query.txt')

    def drop_table(table):
        drop_table_query = f"DROP TABLE IF EXISTS {table}"
        return drop_table_query
    
    def create_table(table_query, table_name):
        table_query.format(table_name)
        return table_query
    
    def read_file(file_path):
        pass

    def get_query(file_path):
        pass