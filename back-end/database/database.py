import sqlite3
import os
from flask import g

class Queries():
    def select_all(self, table_name):
        self.query = f"SELECT * FROM {table_name}"
        return self.query

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
    def return_all(database_connection, cursor_object, table_name):
        cursor_object.execute(Queries().select_all(table_name))
        data = cursor_object.fetchall()
        database_connection.commit()
        return data
    
    @staticmethod
    def get_system_data(database_connection, cursor_object):
        return SMAH().return_all(database_connection, cursor_object, 'acSystemData')