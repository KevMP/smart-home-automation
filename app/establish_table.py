import sqlite3
import os

class Table():
    APPLICATION_FOLDER = 'app'
    DATABASES_FOLDER = os.path.join(APPLICATION_FOLDER, 'databases')
    BACKUP_SCHEMAS_FOLDER = os.path.join(DATABASES_FOLDER, 'backup_schemas')
    SENSOR_DATA_TABLE_CREATION_QUERY = os.path.join(BACKUP_SCHEMAS_FOLDER, 'sensor_data_table_creation_query.txt')

    def drop_table(self, table):
        self.drop_table_query = f"DROP TABLE IF EXISTS {table}"
        return self.drop_table_query
    
    def create_table(self, table_query, table_name):
        table_query.format(table_name)
        return table_query
    
    def read_file(self, file_path):
        self.file = open(file_path, 'r')
        self.data = self.file.read()
        self.file.close()

        return self.data

    def get_query(self, file_path):
        pass