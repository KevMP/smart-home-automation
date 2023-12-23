import sqlite3 as sql
class Database:
    def __init__(self):
        try:
            self.database_connection = sql.connect("C:\\Users\\alfon\\Documents\\repositories\\smart-home-automation\\local\\database.db")
            self.cursor = self.database_connection.cursor()
            print("Database connection successful.")
        except sql.Error as error_message:
            print(f"Error connecting to the database: {error_message}")
            self.database_connection = None
            self.cursor = None
    
    def updateDatabase(self, query):
        if not self.database_connection:
            print("Cannot update database. Database connection not available.")
            return None
        else:
            self.cursor.execute(self.insert_query)
            self.database_connection.commit()
            print("DATABASE UPDATED")

    def closeConnection(self):
        if self.database_connection:
            self.database_connection.close()
            print("Database connection closed.")