import os
import time
import sqlite3

class Read():
    def get_current_time(self):
        self.current_time = time.strftime("%m-%d-%Y-%H-%M-%S")
        return self.current_time

    def get_timestamp(self, cursor_object, table_name, current_time):
        self.timestamp_query = f'''SELECT timeStamp FROM {table_name}
                                   WHERE timeStamp = {current_time}'''
        cursor_object.execute(self.timestamp_query)
        return cursor_object[0]
    
    def get_running_time(self, cursor_object, current_time):
        self.running_time_query = f'''SELECT runningTime FROM acSystemData
                                   WHERE timeStamp = {current_time}'''
        cursor_object.execute(self.running_time_query)
        return cursor_object[0]
    
    def get_temperature(self, cursor_object, current_time="111"):
        self.temperature_query = f'''SELECT temperature FROM sensorData
                                     WHERE timeStamp = {current_time}'''
        cursor_object.execute(self.temperature_query)
        self.temperature = (cursor_object.fetchall())
        return self.temperature