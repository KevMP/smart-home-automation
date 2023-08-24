import sqlite3
import os

class Query():
    ## The following are the constant file paths for the database.

    APPLICATION_FOLDER = 'app'
    DATABASES_FOLDER = os.path.join(APPLICATION_FOLDER, 'databases')
    BACKUP_SCHEMAS_FOLDER = os.path.join(DATABASES_FOLDER, 'backup_schemas')

    AC_SYSTEM_DATA_CREATION_QUERY = os.path.join(BACKUP_SCHEMAS_FOLDER, 'ac_system_data_creation_query.txt')
    SENSOR_DATA_CREATION_QUERY = os.path.join(BACKUP_SCHEMAS_FOLDER, 'sensor_data_creation_query.txt')
    USER_DATA_CREATION_QUERY = os.path.join(BACKUP_SCHEMAS_FOLDER, 'user_data_creation_query.txt')

    ## The following are the constants for the table names. This
    ## is established in case we want to change the name of the tables,
    ## or include new ones.

    AC_SYSTEM_DATA_TABLE = 'acSystemData'
    SENSOR_DATA_TABLE = 'sensorData'
    USER_DATA_TABLE = 'userData'

    ## The drop table function will 'delete' the database, create
    ## table query will create a query to make a new database.

    ## By keeping track of the creation schemas we can create the
    ## databases from scratch if we were to ever accidentally delete
    ## them, or needed a fresh start.

    def drop_table(self, table):
        self.drop_table_query = f"DROP TABLE IF EXISTS {table}"
        return self.drop_table_query
    
    def create_table_query(self, table_query, table_name):
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

class Table():
    ## The following are functions to drop the table,
    ## this is used to reset the table back to its original
    ## empty self.

    def drop_ac_system_table(self):
        return Query().drop_table(Query().AC_SYSTEM_DATA_TABLE)

    def drop_sensor_table(self):
        return Query().drop_table(Query().SENSOR_DATA_TABLE)
    
    def drop_user_table(self):
        return Query().drop_table(Query().USER_DATA_TABLE)
    
    ## The following are for creating the tables using
    ## the stored creation queries.

    def create_ac_system_table(self):
        self.creation_query = Query().get_query(Query().AC_SYSTEM_DATA_CREATION_QUERY)
        return Query().create_table_query(self.creation_query, Query().AC_SYSTEM_DATA_TABLE)

    def create_sensor_table(self):
        self.creation_query = Query().get_query(Query().SENSOR_DATA_CREATION_QUERY)
        return Query().create_table_query(self.creation_query, Query().SENSOR_DATA_TABLE)

    def create_user_table(self):
        self.creation_query = Query().get_query(Query().USER_DATA_CREATION_QUERY)
        return Query().create_table_query(self.creation_query, Query().USER_DATA_TABLE)
    
    def reset_all_tables(self):
        pass