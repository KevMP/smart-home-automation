import sqlite3

DATABASE = 'SHAS.db'

TABLE_SYSTEM_DATA = 'acSystemData'
TABLE_SENSOR_DATA = 'sensorData'
TABLE_USER_DATA = 'userData'

NEW_TEMPERATURE = 94.0
USER_ID = '1'
TIME_STAMP = '14'

def add_data():
    insert_query = f"INSERT INTO {TABLE_SENSOR_DATA} (temperature, userId, timestamp) VALUES (?, ?, ?)"
    cursor.execute(insert_query, (NEW_TEMPERATURE, USER_ID, TIME_STAMP))
    connection.commit()

def view_data(table):
    select_query = f"SELECT * FROM {table}"
    cursor.execute(select_query)

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

## The for loop would insert data to the table sensorData
## range n amount of times.

for iterator in range(10):
    add_data()

cursor.close()
connection.close()