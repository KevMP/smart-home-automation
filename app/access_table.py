import sqlite3
import os

class Database():
    ## Constant pathing variables.
    APPLICATION_FOLDER = 'app'
    DATABASES_FOLDER = os.path.join(APPLICATION_FOLDER, 'databases')

    DATABASE_FILE = os.path.join(DATABASES_FOLDER, 'SHAS.db')
    AC_SYSTEM_DATA_TABLE = 'acSystemData'
    SENSOR_DATA_TABLE = 'sensorData'
    USER_DATA_TABLE = 'userData'

    ## The following function will create a connection
    ## to the database, this will enable the features
    ## to view all the data, fields, etc inside of that
    ## database.
    ## Note that a cursor object has to be created to
    ## execute sql queries to access the data.

    def create_connection(self, database_file):
        self.connection = sqlite3.connect(database_file)
        return self.connection
    
    ## The following will capture all fields in the
    ## database.
    ## And will allow the functionality of printing
    ## out all the field data.

    def select_all_fields(self, database_connection, table_name):
        self.cursor = database_connection.cursor()
        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()

    def print_all_fields(self, table_name):
        self.connection = self.create_connection(self.DATABASE_FILE)
        self.fields = self.select_all_fields(self.connection, table_name)

        for row in self.fields:
            print(row)

        self.connection.close()

class Timestamp():
    ## The following are to be used to gather
    ## the specific timestamp data.

    def get_timestamp(self):
        pass

    def get_month(self):
        pass

    def get_day(self):
        pass

    def get_year(self):
        pass

    def get_hour(self):
        pass

    def get_minute(selF):
        pass

    def get_second(self):
        pass
