import sqlite3
import os

class Table():
    APPLICATION_FOLDER = 'app'
    DATABASES_FOLDER = os.path.join(APPLICATION_FOLDER, 'databases')
    BACKUP_SCHEMAS_FOLDER = os.path.join(DATABASES_FOLDER, 'backup_schemas')

    SENSOR_DATA_TABLE_CREATION_QUERY = os.path.join(BACKUP_SCHEMAS_FOLDER, 'sensor_data_creation_query.txt')
    USER_DATA_TABLE_CREATION_QUERY = os.path.join(BACKUP_SCHEMAS_FOLDER, 'user_data_creation_query.txt')

    ## The drop table function will 'delete' the database, create
    ## table will create a new database.

    ## By keeping track of the creation schemas we can create the
    ## databases from scratch if we were to ever accidentally delete
    ## them, or needed a fresh start.

    def drop_table(self, table):
        self.drop_table_query = f"DROP TABLE IF EXISTS {table}"
        return self.drop_table_query
    
    def create_table(self, table_query, table_name):
        table_query.format(table_name)
        return table_query
    
    ## The following will read data and return the
    ## query to its function call.

    def read_file(self, file_path):
        self.file = open(file_path, 'r')
        self.data = self.file.read()
        self.file.close()

        return self.data

    def get_query(self, file_path):
        return self.read_file(file_path)
    
    ## The following will be functions to a table
    ## in terms of creating and dropping tables.

    def drop_sensor_table(self):
        return self.drop_table('sensorData')

    def create_sensor_table(self):
        self.creation_query = self.get_query(self.SENSOR_DATA_TABLE_CREATION_QUERY)
        self.create_table(self.creation_query, 'sensorData')