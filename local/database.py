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
    
    def getMinimumPreferredTemperature(self, profile_identification):
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

    def getMaximumPreferredTemperature(self, profile_identification):
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

# Example usage
if __name__ == "__main__":
    print('creating database object')
    db = Database()
    db.createProfilesTable()
    db.createModelTable()
    db.createSensorTable()
    db.getMinimumPreferredTemperature(0)
    db.closeConnection()