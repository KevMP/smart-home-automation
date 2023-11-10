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

# Example usage
if __name__ == "__main__":
    print('creating database object')
    db = Database()
    db.createProfilesTable()
    db.createModelTable()
    db.createSensorTable()
    db.closeConnection()