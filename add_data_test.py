import sqlite3

DATABASE = 'SHAS.db'

TABLE_SYSTEM_DATA = 'acSystemData'
TABLE_SENSOR_DATA = 'sensorData'
TABLE_USER_DATA = 'userData'

def add_sensor_data():
    pass

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

cursor.close()
connection.close()