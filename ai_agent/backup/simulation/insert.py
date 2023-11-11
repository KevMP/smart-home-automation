import sqlite3
import os

class Database:
    def __init__(self):
        self.dbPath = os.path.join('simulation', 'SHAS.db')
        self.connection = sqlite3.connect(self.dbPath)
        self.cursor = self.connection.cursor()

    def insertSensorData(self, temperature, user_identification, time_stamp):
        self.sql_query = f'''INSERT INTO sensorData (temperature, userId, timestamp)
                             VALUES (?, ?, ?);'''
        self.cursor.execute(self.sql_query, (temperature, user_identification, time_stamp))
        self.connection.commit()

    def close(self):
        self.connection.close()

# Create the database object
database = Database()

# Insert data into the table
database.insertSensorData(45, 10000, '1122')

# Close the database connection when done
database.close()
