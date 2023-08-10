import sqlite3

DATABASE = 'SHAS.db'

TABLE_SYSTEM_DATA = 'acSystemData'
TABLE_SENSOR_DATA = 'sensorData'
TABLE_USER_DATA = 'userData'

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

new_temperature = 94.0
user_id = '1'
timestamp = '14'

insert_query = f"INSERT INTO {TABLE_SENSOR_DATA} (temperature, userId, timestamp) VALUES (?, ?, ?)"

cursor.execute(insert_query, (new_temperature, user_id, timestamp))
connection.commit()

cursor.close()
connection.close()