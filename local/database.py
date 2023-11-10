import sqlite3

class Database():
    def __init__(self, db_name='data.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def createProfilesTable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS profiles (
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

    def close(self):
        self.conn.close()

# Example usage
if __name__ == "__main__":
    db = Database()
    db.createProfilesTable()
    db.createModelTable()
    db.createSensorTable()
    db.close()
