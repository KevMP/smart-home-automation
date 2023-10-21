import sqlite3

class Connection():
    def __init__(self, databasePath):
        self.connection = sqlite3.connect(databasePath)
        self.cursor = self.connection.cursor()
    
    def closeConnection(self):
        self.cursor.close()
        self.connection.close()

database = Connection('SHAS.db')