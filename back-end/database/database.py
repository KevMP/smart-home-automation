import sqlite3
import os
from flask import g

class Query():
    def select_all(self, table_name):
        self.query = f"SELECT * FROM {table_name}"
        return self.query
    
    def return_all(self, database_connection, cursor_object, table_name):
        cursor_object.execute(Query().select_all(table_name))
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

    ## The following functions are returning all the data in a table, at once.
    ## The get_all_table_data function inserts all the table data into a hash
    ## map so that it can be jsonified.
    @staticmethod
    def get_all_system_data(database_connection, cursor_object):
        return Query().return_all(database_connection, cursor_object, 'acSystemData')
    @staticmethod
    def get_all_sensor_data(database_connection, cursor_object):
        return Query().return_all(database_connection, cursor_object, 'sensorData')
    @staticmethod
    def get_all_user_data(database_connection, cursor_object):
        return Query().return_all(database_connection, cursor_object, 'userData')
    @staticmethod
    def get_all_user_account_data(database_connection, cursor_object):
        return Query().return_all(database_connection, cursor_object, 'userAccount')
    @staticmethod
    def get_all_table_data(db, cursor):
        table_hash_map = {}
        table_list = [SMAH().get_all_system_data(db, cursor),
                     SMAH().get_all_sensor_data(db, cursor),
                     SMAH().get_all_user_data(db, cursor),
                     SMAH().get_all_user_account_data(db, cursor)]
        
        for table in range(len(table_list)):
            table_hash_map[table] = table_list[table]

        return table_hash_map