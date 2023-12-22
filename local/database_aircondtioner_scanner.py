from database_root import *
import time

class Airconditioner(Database):
    def __init__(self):
        super().__init__()
        self.command_to_ac = ""  # Initialize command_to_ac to an empty string

    def get_command_from_ai(self):
        select_query = "SELECT command FROM TemperatureModel ORDER BY timestamp DESC LIMIT 1;"
        self.cursor.execute(select_query)
        result = self.cursor.fetchone()
        if result:
            self.command_to_ac = result[0]  # Set command_to_ac with the command from AI
            return self.command_to_ac
        else:
            # If no command found, you might want to handle this case.
            return None

    def write_command_to_ac(self):
        if self.command_to_ac:
            insert_query = "INSERT INTO Airconditioner (command) VALUES (?);"
            self.cursor.execute(insert_query, (self.command_to_ac,))
            self.database_connection.commit()
            # Command has been written to the database. If you need to do something here, add your code.
        else:
            # If no command to write, handle this case if necessary.
            pass

    def close_connection(self):
        self.closeConnection()

def database_airconditioner_scanner(scan_interval=0.5):  # Scan every half second
    ac = Airconditioner()
    try:
        while True:
            command = ac.get_command_from_ai()
            if command:
                ac.write_command_to_ac()
            time.sleep(scan_interval)  # Wait for half a second before the next scan
    except KeyboardInterrupt:
        # Here you can handle the manual stop if needed.
        pass
    finally:
        ac.close_connection()
        # Here you can handle the closure of database connection if needed.

if __name__ == "__main__":
    database_airconditioner_scanner()
