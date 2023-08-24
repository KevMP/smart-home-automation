import os
import sqlite3
from access_table import Database

class Insert():
    app_folder = 'app'
    database_folder = os.path.join(app_folder, 'databases')
    database_file = os.path.join(database_folder, 'SHAS.db')

    system_table = Database().ac_system_data_table
    sensor_table = Database().sensor_data_table
    user_table = Database().user_data_table

    ## The following functions will create a sql query that will be executed
    ## by the cursor in our main function for this class.
    
    ## Note, that when we are generating fake data we can use these functions
    ## to create that faked data.

    def insert_ac_system_data(self, running_time, time_stamp, user_identification):
        self.sql_query = f'''INSERT INTO {self.system_table}
                             VALUES ({running_time}, {time_stamp}, {user_identification}'''
        return self.sql_query

    def insert_sensor_data(self, temperature, user_identification, time_stamp):
        self.sql_query = f'''INSERT INTO {self.sensor_table}
                             VALUES ({temperature}, {user_identification}, {time_stamp})'''
        return self.sql_query
    
    def insert_user_data(self, preferred_temperature, number_of_residents):
        self.sql_query = ''
        return self.sql_query

    ## The cursor object will be executing all sql statements,
    ## note that a database connection must be made before executing
    ## the sql code.

    def insert_all_data(self):
        database_connection = Database().create_connection("SHAS.db")
        sql_cursor = database_connection.cursor()

        sql_cursor.execute(self.insert_ac_system_data())
        sql_cursor.execute(self.insert_sensor_data())
        sql_cursor.execute(self.insert_user_data())

        sql_cursor.close()
        database_connection.close()