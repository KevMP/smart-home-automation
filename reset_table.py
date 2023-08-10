import sqlite3

DATABASE = 'SHAS.db'

TABLE_SYSTEM_DATA = 'acSystemData'
TABLE_SENSOR_DATA = 'sensorData'
TABLE_USER_DATA = 'userData'

def create_sensor_data_table():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS {} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature NUMERIC,
    userId TEXT,
    timestamp TEXT
    )
'''.format(TABLE_SENSOR_DATA)