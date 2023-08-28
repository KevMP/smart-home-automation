import sqlite3
import os
from flask import g

class SMAH():
    ac_system_data_table = 'acSystemData'
    sensor_data_table = 'sensorData'
    user_data_table = 'userData'

    table_columns = [ac_system_data_table, sensor_data_table, user_data_table]
    
    user_account = 'userAccount'
    """
    user_id: primary key, text, unique
    email: text, unique
    password: text
    first_name: text
    last_name: text
    """

    @staticmethod
    def get_connection():
        database_file = os.path.join(r'\databases', 'SHAS.db')
        if 'db' not in g:
            g.db = sqlite3.connect(os.getcwd() + database_file)
        return g.db

    @staticmethod
    def close_connection():
        db = g.pop('db', None)
        if db is not None:
            db.close()

    ## The following will be to select all data from each table.
    ## I will be creating separate functions for each respective
    ## table, systemData, userData, etc.

    def select_all_user_data(self):
        pass

    def select_all_data(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        result = [cursor.execute(f"SELECT * FROM {column}") for column in self.table_columns]
        result = cursor.fetchall()

        cursor.close()
        return result

    def print_all_data(self):
        data = self.select_all_data()
        print(data)
        
    def populate_with_fake_data(self):
        pass
        
    def deletes_all_data(self):
        pass



    def insert_user(self):
        pass
        
    def get_user(self, email):
        pass

    def populate_with_fake_users(self):
        pass