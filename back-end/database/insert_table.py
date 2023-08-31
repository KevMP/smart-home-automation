import os
import sqlite3
from database import SMAH
from flask import g

class Insert():
    backend_folder = 'back-end'
    database_folder = os.path.join(backend_folder, 'databases')
    database_file = os.path.join(database_folder, 'SHAS.db')

    system_table = 'acSystemData'
    sensor_table = 'sensorData'
    user_table = 'userData'

    ## The following functions will create a sql query that will be executed
    ## by the cursor in our main function for this class.
    
    ## Note, that when we are generating fake data we can use these functions
    ## to create that faked data.

    def create_insert_ac_system_data_query(self, running_time, time_stamp, user_identification):
        self.sql_query = f'''INSERT INTO {self.system_table} (runningTime, timeStamp, userId)
                             VALUES ({running_time}, {time_stamp}, {user_identification});'''
        return self.sql_query

    def create_insert_sensor_data_query(self, temperature, user_identification, time_stamp):
        self.sql_query = f'''INSERT INTO {self.sensor_table} (temperature, userId, timestamp)
                             VALUES ({temperature}, {user_identification}, {time_stamp});'''
        return self.sql_query
    
    def create_insert_user_data_query(self, preferred_temperature, number_of_residents):
        self.sql_query = f'''INSERT INTO {self.user_table} (preferredTemperature, numberOfResidents)
                             VALUES ({preferred_temperature}, {number_of_residents});'''
        return self.sql_query

    ## The cursor object will be executing all sql statements,
    ## note that a database connection must be made before executing
    ## the sql code.

    def create_connection(self, database_path):
        self.database_connection = sqlite3.connect(database_path)
        return self.database_connection
    
    ## The following function will insert the data generated from the queries
    ## above.

    def insert_ac_system_data(self, running_time, time_stamp, user_identification):
        self.database_connection = self.create_connection(self.database_file)
        self.sql_cursor = self.database_connection.cursor()

        self.insert_query = self.create_insert_ac_system_data_query(running_time, time_stamp, user_identification)
        self.sql_cursor.execute(self.insert_query)
        
        self.database_connection.commit()
        self.sql_cursor.close()
        self.database_connection.close()

    def insert_all_data(self):
        self.database_connection = self.create_connection(self.database_file)
        self.sql_cursor = self.database_connection.cursor()

        ## An example of how to execute a sql cursor for inserting
        ## data to the tables is shown below.

        self.sql_cursor.execute(self.insert_user_data("72", 2))
        self.database_connection.commit()

        self.sql_cursor.close()
        self.database_connection.close()