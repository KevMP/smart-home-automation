import sqlite3
import os
from flask import g

class Queries():
    def select_all(self, table_name):
        self.query = f"SELECT * FROM {table_name}"
        return self.query
    
    def return_all(self, database_connection, cursor_object, table_name):
        cursor_object.execute(Queries().select_all(table_name))
        self.data = cursor_object.fetchall()
        database_connection.commit()
        return self.data

class SMAH():
    @staticmethod
    def get_connection():
        if 'db' not in g:
            g.db = sqlite3.connect('databases/SHAS.db')
        return g.db

    @staticmethod
    def close_connection():
        db = g.pop('db', None)
        if db is not None:
            db.close()

    @staticmethod
    def create_connection():
        database_connection = sqlite3.connect('databases/SHAS.db')
        return database_connection
    
    @staticmethod
    def get_system_data(database_connection, cursor_object):
        return Queries().return_all(database_connection, cursor_object, 'acSystemData')
    
    @staticmethod
    def get_sensor_data(database_connection, cursor_object):
        return Queries().return_all(database_connection, cursor_object, 'sensorData')

    @staticmethod
    def get_user_data(database_connection, cursor_object):
        return Queries().return_all(database_connection, cursor_object, 'userData')

    @staticmethod
    def get_user_account_data(database_connection, cursor_object):
        return Queries().return_all(database_connection, cursor_object, 'userAccount')