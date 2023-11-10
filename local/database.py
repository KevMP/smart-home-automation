import sqlite3

class Database():
    def __init__(self, db_name='local/data.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def closeConnection(self):
        self.conn.close()

    def createProfilesTable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS profile (
                profile_id INTEGER PRIMARY KEY,
                min_preferred_temperature REAL,
                max_preferred_temperature REAL
            )
        ''')
        self.conn.commit()

    def createModelTable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS model (
                timestamp TEXT,
                profile_id INTEGER,
                current_move TEXT
            )
        ''')
        self.conn.commit()

    def createSensorTable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sensor (
                timestamp TEXT,
                sensor_id INTEGER,
                temperature REAL,
                humidity REAL
            )
        ''')
        self.conn.commit()
    
    def removeTable(self, table_name):
        try:
            self.cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
            self.conn.commit()
            print(f'Table "{table_name}" removed successfully.')
        except sqlite3.Error as e:
            print(f'Error removing table "{table_name}": {e}')

    def removeAllTables(self):
        self.removeTable('sensor')
        self.removeTable('profile')
        self.removeTable('model')
        self.closeConnection()
    
    def getMinimumPreferredTemperature(self, profile_identification: int):
        try:
            self.cursor.execute('SELECT min_preferred_temperature FROM profile WHERE profile_id = ?', (profile_identification,))
            result = self.cursor.fetchone()
            if result:
                return result[0]  # Extract the preferred value
            else:
                print(f"Profile with ID {profile_identification} not found.")
                return None
        except sqlite3.Error as e:
            print(f'Error retrieving minimum preferred temperature: {e}')
            return None

    def getMaximumPreferredTemperature(self, profile_identification: int):
        try:
            self.cursor.execute('SELECT max_preferred_temperature FROM profile WHERE profile_id = ?', (profile_identification,))
            result = self.cursor.fetchone()
            if result:
                return result[0]  # Extract the preferred value
            else:
                print(f"Profile with ID {profile_identification} not found.")
                return None
        except sqlite3.Error as e:
            print(f'Error retrieving maximum preferred temperature: {e}')
            return None
    
    def setMinimumPreferredTemperature(self, profile_identification, value):
        try:
            # Check if the profile exists
            self.cursor.execute('SELECT profile_id FROM profile WHERE profile_id = ?', (profile_identification,))
            existing_profile = self.cursor.fetchone()

            if existing_profile:
                # Profile exists, update the value
                self.cursor.execute('UPDATE profile SET min_preferred_temperature = ? WHERE profile_id = ?', (value, profile_identification))
            else:
                # Profile does not exist, create a new profile
                self.cursor.execute('INSERT INTO profile (profile_id, min_preferred_temperature, max_preferred_temperature) VALUES (?, ?, ?)', (profile_identification, value, 0.0))

            self.conn.commit()
            print(f'Minimum preferred temperature set for Profile ID {profile_identification}: {value}')
        except sqlite3.Error as e:
            print(f'Error setting minimum preferred temperature: {e}')

    def setMaximumPreferredTemperature(self, profile_identification: int, value: float):
        try:
            # Check if the profile exists
            self.cursor.execute('SELECT profile_id FROM profile WHERE profile_id = ?', (profile_identification,))
            existing_profile = self.cursor.fetchone()

            if existing_profile:
                # Profile exists, update the value
                self.cursor.execute('UPDATE profile SET max_preferred_temperature = ? WHERE profile_id = ?', (value, profile_identification))
            else:
                # Profile does not exist, create a new profile
                self.cursor.execute('INSERT INTO profile (profile_id, min_preferred_temperature, max_preferred_temperature) VALUES (?, ?, ?)', (profile_identification, 0.0, value))

            self.conn.commit()
            print(f'Maximum preferred temperature set for Profile ID {profile_identification}: {value}')
        except sqlite3.Error as e:
            print(f'Error setting maximum preferred temperature: {e}')

    def setCurrentMove(self, timestamp: str, profile_identification: int, model_temperature_direction: str):
        try:
            self.cursor.execute('INSERT INTO model (timestamp, profile_id, current_move) VALUES (?, ?, ?)', (timestamp, profile_identification, model_temperature_direction))
            self.conn.commit()
            print(f"Current move set for Profile ID {profile_identification} at timestamp {timestamp}: {model_temperature_direction}")
        except sqlite3.Error as e:
            print(f'Error setting current move: {e}')

    def getCurrentMove(self):
        try:
            self.cursor.execute('SELECT current_move FROM model ORDER BY timestamp DESC LIMIT 1')
            result = self.cursor.fetchone()
            if result:
                return result[0]  # Extract the most recent current move
            else:
                print("No current move records found.")
                return None
        except sqlite3.Error as e:
            print(f'Error getting current move: {e}')
            return None

    def setSensorHumidity(self, timestamp: str, sensor_identification: int, temperature: float, humidity: float):
        try:
            # Check if the timestamp and sensor identification combination already exists in the 'sensor' table
            self.cursor.execute('SELECT timestamp FROM sensor WHERE timestamp = ? AND sensor_id = ?', (timestamp, sensor_identification))
            existing_data = self.cursor.fetchone()

            if existing_data:
                print(f"Sensor data for timestamp {timestamp} and sensor ID {sensor_identification} already exists.")
            else:
                # Timestamp and sensor identification do not exist, insert the new sensor data
                self.cursor.execute('INSERT INTO sensor (timestamp, sensor_id, temperature, humidity) VALUES (?, ?, ?, ?)', (timestamp, sensor_identification, temperature, humidity))
                self.conn.commit()
                print(f"Sensor data recorded for timestamp {timestamp}, Sensor ID {sensor_identification}: Temperature = {temperature}, Humidity = {humidity}")
        except sqlite3.Error as e:
            print(f'Error setting sensor data: {e}')

# Example usage
if __name__ == "__main__":
    print('creating database object')
    db = Database()
    db.setMinimumPreferredTemperature(0, 72)
    db.setMaximumPreferredTemperature(0, 75)
    db.closeConnection()