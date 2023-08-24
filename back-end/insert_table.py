import os
import sqlite3
from access_table import Database

class Insert():
    app_folder = 'back-end'
    database_folder = os.path.join(app_folder, 'databases')
    database_file = os.path.join(database_folder, 'SHAS.db')

    system_table = 'acSystemData'
    sensor_table = 'sensorData'
    user_table = 'userData'

    ## The following functions will create a sql query that will be executed
    ## by the cursor in our main function for this class.
    
    ## Note, that when we are generating fake data we can use these functions
    ## to create that faked data.

    def insert_ac_system_data(self, running_time, time_stamp, user_identification):
        self.sql_query = f'''INSERT INTO {self.system_table} (runningTime, timeStamp, userId)
                             VALUES ({running_time}, {time_stamp}, {user_identification});'''
        return self.sql_query

    def insert_sensor_data(self, temperature, user_identification, time_stamp):
        self.sql_query = f'''INSERT INTO {self.sensor_table} (temperature, userId, timestamp)
                             VALUES ({temperature}, {user_identification}, {time_stamp});'''
        return self.sql_query
    
    def insert_user_data(self, user_identification, preferred_temperature, number_of_residents):
        self.sql_query = f'''INSERT INTO {self.user_table} (userId, preferredTemperature, numberOfResidents)
                             VALUES ({user_identification}, {preferred_temperature}, {number_of_residents});'''
        return self.sql_query

    ## The cursor object will be executing all sql statements,
    ## note that a database connection must be made before executing
    ## the sql code.

    def insert_all_data(self):
        self.database_connection = sqlite3.connect(self.database_file)
        self.sql_cursor = self.database_connection.cursor()

        self.sql_cursor.execute(self.insert_ac_system_data("00-11-00", "12-00", "111"))
        self.sql_cursor.execute(self.insert_sensor_data(12.1, "111", "12-00"))
        self.sql_cursor.execute(self.insert_user_data(111, 12.1, 2))

        self.sql_cursor.execute("SELECT * FROM userData")

        self.sql_cursor.close()
        self.database_connection.close()

Insert().insert_all_data()