import sqlite3
import os
from flask import g

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