import os
import sqlite3
from access_table import Database

class Insert():
    app_folder = 'app'
    database_folder = os.path.join(app_folder, 'databases')
    database_file = os.path.join(database_folder, 'SHAS.db')

    def insert_ac_system_data(self, running_time, time_stamp, user_identification):
        pass

    def insert_sensor_data(self, temperature, user_identification, time_stamp):
        pass
    
    def insert_user_data(self, preferred_temperature, number_of_residents):
        pass

    ## The cursor object will be executing all sql statements,
    ## note that a database connection must be made before executing
    ## the sql code.

    def insert_all_data(self):
        database_connection = Database().create_connection("SHAS.db")
        sql_cursor = database_connection.cursor()

        sql_cursor.close()
        database_connection.close()