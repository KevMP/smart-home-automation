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
    
    def writeToDatabase(self, query):
        if not self.database_connection:
            print("Cannot update database. Database connection not available.")
            return None
        else:
            self.cursor.execute(query)
            self.database_connection.commit()
            print("DATABASE WRITE")
    
    def getFromDatabase(self, query):
        if not self.database_connection:
            print("Cannot update database. Database connection not available.")
            return None
        else:
            print(f"Executing query: {query}")
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            self.database_connection.commit()
            print(f"DATABASE READ {result}")
            return result

    def closeConnection(self):
        if self.database_connection:
            self.database_connection.close()
            print("Database connection closed.")