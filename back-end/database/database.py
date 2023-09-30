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