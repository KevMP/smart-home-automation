import os
import sqlite3
from access_table import Database

class Insert():
    app_folder = 'app'
    database_folder = os.path.join(app_folder, 'databases')