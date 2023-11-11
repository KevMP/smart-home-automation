import sqlite3

class Database:
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
    
    def createAirconditionerTable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS airconditioner (
                timestamp TEXT,
                target_temperature REAL
            )
        ''')
        self.conn.commit()

    def createAllTables(self):
        self.createProfilesTable()
        self.createModelTable()
        self.createSensorTable()
        self.createAirconditionerTable()

    def getTargetTemperature(self):
        try:
            self.cursor.execute('SELECT target_temperature FROM airconditioner ORDER BY timestamp DESC LIMIT 1')
            result = self.cursor.fetchone()
            return int(result[0]) if result else None
        except (sqlite3.Error, TypeError) as e:
            print(f'Error getting target temperature: {e}')
            return None

    def setTargetTemperature(self, timestamp: str, target_temperature: float):
        try:
            # Check if the timestamp exists in the 'airconditioner' table
            self.cursor.execute('SELECT target_temperature FROM airconditioner WHERE timestamp = ?', (timestamp,))
            existing_temperature = self.cursor.fetchone()

            if existing_temperature and existing_temperature[0] == target_temperature:
                print(f"Target temperature for timestamp {timestamp} already set to {target_temperature}.")
            else:
                # Timestamp does not exist or the temperature is different, insert the new target temperature
                self.cursor.execute('INSERT INTO airconditioner (timestamp, target_temperature) VALUES (?, ?)', (timestamp, target_temperature))
                self.conn.commit()
                print(f"Target temperature set for timestamp {timestamp}: {target_temperature}")
        except sqlite3.Error as e:
            print(f'Error setting target temperature: {e}')

    def removeTable(self, table_name: str):
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

    def getCurrentProfile(self):
        try:
            with open('local/currentProfile.txt', 'r') as file:
                profile_identification = file.read()
                return int(profile_identification) if profile_identification.isdigit() else None
        except (IOError, ValueError) as e:
            print(f'Error reading current profile: {e}')
            return None

    def setCurrentProfile(self, profile_identification: int):
        try:
            with open('currentProfile.txt', 'w') as file:
                file.write(str(profile_identification))
            print(f'Current profile set to {profile_identification}.')
        except IOError as e:
            print(f'Error setting current profile: {e}')

    def getAllProfilesAsArray(self):
        try:
            self.cursor.execute('SELECT DISTINCT profile_id FROM profile')
            result = self.cursor.fetchall()
            return [row[0] for row in result] if result else []
        except sqlite3.Error as e:
            print(f'Error getting all profiles: {e}')
            return []

    def doesProfileExist(self, profile_identification: int):
        try:
            self.cursor.execute('SELECT COUNT(*) FROM profile WHERE profile_id = ?', (profile_identification,))
            result = self.cursor.fetchone()
            return result[0] > 0 if result else False
        except sqlite3.Error as e:
            print(f'Error checking profile existence: {e}')
            return False

    def deleteProfile(self, profile_identification: int):
        try:
            self.cursor.execute('DELETE FROM profile WHERE profile_id = ?', (profile_identification,))
            self.conn.commit()
            print(f'Profile with ID {profile_identification} deleted successfully.')
        except sqlite3.Error as e:
            print(f'Error deleting profile: {e}')

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
    
    def setMinimumPreferredTemperature(self, profile_identification: int, value: float):
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

    def recordSensorData(self, timestamp: str, sensor_identification: int, temperature: float, humidity: float):
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

    def getTemperature(self, sensor_identification: int):
        try:
            self.cursor.execute('SELECT temperature FROM sensor WHERE sensor_id = ? ORDER BY timestamp DESC LIMIT 1', (sensor_identification,))
            result = self.cursor.fetchone()
            if result:
                return result[0]  # Extract the most recent temperature
            else:
                print(f"No temperature data found for Sensor ID {sensor_identification}.")
                return None
        except sqlite3.Error as e:
            print(f'Error getting temperature data: {e}')
            return None

    def getHumidity(self, sensor_identification: int):
        try:
            self.cursor.execute('SELECT humidity FROM sensor WHERE sensor_id = ? ORDER BY timestamp DESC LIMIT 1', (sensor_identification,))
            result = self.cursor.fetchone()
            if result:
                return result[0]  # Extract the most recent humidity
            else:
                print(f"No humidity data found for Sensor ID {sensor_identification}.")
                return None
        except sqlite3.Error as e:
            print(f'Error getting humidity data: {e}')
            return None

    def getMedianTemperature(self):
        try:
            # Retrieve the most recent timestamp common to all sensors
            self.cursor.execute('SELECT timestamp FROM sensor GROUP BY timestamp HAVING COUNT(*) = (SELECT COUNT(DISTINCT sensor_id) FROM sensor)')
            timestamp = self.cursor.fetchone()

            if timestamp:
                timestamp = timestamp[0]

                # Retrieve the temperature data for the common timestamp
                self.cursor.execute('SELECT temperature FROM sensor WHERE timestamp = ?', (timestamp,))
                result = self.cursor.fetchall()
                if result:
                    temperature_values = [row[0] for row in result]
                    median_temperature = sorted(temperature_values)[len(temperature_values) // 2]
                    return median_temperature
                else:
                    print("No temperature data found for the common timestamp.")
                    return None
            else:
                print("No common timestamp found for all sensors.")
                return None
        except sqlite3.Error as e:
            print(f'Error getting median temperature data: {e}')
            return None

    def getMedianHumidity(self):
        try:
            # Retrieve the most recent timestamp common to all sensors
            self.cursor.execute('SELECT timestamp FROM sensor GROUP BY timestamp HAVING COUNT(*) = (SELECT COUNT(DISTINCT sensor_id) FROM sensor)')
            timestamp = self.cursor.fetchone()

            if timestamp:
                timestamp = timestamp[0]

                # Retrieve the humidity data for the common timestamp
                self.cursor.execute('SELECT humidity FROM sensor WHERE timestamp = ?', (timestamp,))
                result = self.cursor.fetchall()
                if result:
                    humidity_values = [row[0] for row in result]
                    median_humidity = sorted(humidity_values)[len(humidity_values) // 2]
                    return median_humidity
                else:
                    print("No humidity data found for the common timestamp.")
                    return None
            else:
                print("No common timestamp found for all sensors.")
                return None
        except sqlite3.Error as e:
            print(f'Error getting median humidity data: {e}')
            return None

# Example usage
if __name__ == "__main__":
    print('creating database object')
    db = Database()
    db.setMinimumPreferredTemperature(1, 50)
    db.setMaximumPreferredTemperature(1, 53)
    profileArray = db.getAllProfilesAsArray()
    print(profileArray)
    db.closeConnection()