import sqlite3
import os
from flask import g

class Database():
    ac_system_data_table = 'acSystemData'
    sensor_data_table = 'sensorData'
    user_data_table = 'userData'

    table_columns = [ac_system_data_table, sensor_data_table, user_data_table]

    @staticmethod
    def get_connection():
        database_file = os.path.join(r'\databases', 'SHAS.db')
        if 'db' not in g:
            g.db = sqlite3.connect(os.getcwd() + database_file)
        return g.db

    @staticmethod
    def close_connection(exception=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()

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
