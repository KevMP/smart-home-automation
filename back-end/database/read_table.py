import os
import time
import sqlite3

class Read():
    def get_current_time(self):
        self.current_time = time.strftime("%m-%d-%Y-%H-%M-%S")
        return self.current_time

    ## The following functions are established with a SQL query, which
    ## will have to be passed the current time from outside of this class.

    ## That way, in our simulation loop we can call the current time
    ## one time per loop instead of per function.

    ## This is where the Ai will get its features from (the input layer
    ## of the neural network).

    def get_timestamp(self, cursor_object, table_name, current_time):
        self.timestamp_query = f'''SELECT timeStamp FROM {table_name}
                                   WHERE timeStamp = {current_time}'''
        
        cursor_object.execute(self.timestamp_query)
        self.timestamp = cursor_object.fetchall()
        
        return self.timestamp
    
    def get_running_time(self, cursor_object, current_time):
        self.running_time_query = f'''SELECT runningTime FROM acSystemData
                                   WHERE timeStamp = {current_time}'''

        cursor_object.execute(self.running_time_query)
        self.running_time = cursor_object.fetchall()
        
        return self.running_time
    
    def get_temperature(self, cursor_object, current_time):
        self.temperature_query = f'''SELECT temperature FROM sensorData
                                     WHERE timeStamp = {current_time}'''
        
        cursor_object.execute(self.temperature_query)
        self.temperature = cursor_object.fetchall()
        
        return self.temperature
    
    ## Make sure to pass the correct user whose preferred temperature
    ## the Ai will try to aim for!!!!!!!!!

    ## Ideally this should be called before the simulation loop runs,
    ## but if you want to change users midway, you can also create
    ## a background process that checks for any user input to change
    ## which user is currently using the ac system.

    def get_preferred_temperature(self, cursor_object, userID):
        self.preferred_temperature_query = f'''SELECT preferredTemperature from userData
                                               WHERE userID = {userID}'''
        
        cursor_object.execute(self.preferred_temperature_query)
        self.preferred_temperature = cursor_object.fetchall()

        return self.preferred_temperature

    def get_number_of_residents(self, cursor_object, userId):
        self.number_of_residents_query = f'''SELECT numberOfResidents from userData
                                       WHERE userID =  {userId}'''
        
        cursor_object.execute(self.number_of_residents)
