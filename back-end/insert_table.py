import os
import sqlite3
from access_table import Database

class Insert():
    app_folder = 'app'
    database_folder = os.path.join(app_folder, 'databases')
    database_file = os.path.join(database_folder, 'SHAS.db')
    
    def insert_data(self, table, field):
        pass

    def insert_all_data(self):
        database_connection = Database().create_connection("SHAS.db")