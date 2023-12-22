from database_root import *
import time
import logging

# Configure logging
logging.basicConfig(filename='airconditioner_commands.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

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
            logging.info(f"Command retrieved from AI: {self.command_to_ac}")
            return self.command_to_ac
        else:
            logging.info("No recent command found.")
            return None

    def write_command_to_ac(self):
        if self.command_to_ac:
            insert_query = "INSERT INTO Airconditioner (command) VALUES (?);"
            self.cursor.execute(insert_query, (self.command_to_ac,))
            self.database_connection.commit()
            logging.info(f"Command written to the database: {self.command_to_ac}")
        else:
            logging.info("No command to write to the Airconditioner table.")

    def close_connection(self):
        self.closeConnection()

def database_airconditioner_scanner(scan_interval=0.5):  # Scan every half second
    """
    Function to continuously scan for commands from the AI and log them.
    
    :param scan_interval: Time in seconds between each scan
    """
    ac = Airconditioner()
    try:
        while True:
            command = ac.get_command_from_ai()
            if command:
                ac.write_command_to_ac()
            time.sleep(scan_interval)  # Wait for half a second before the next scan
    except KeyboardInterrupt:
        logging.info("Scanner stopped manually.")
    finally:
        ac.close_connection()
        logging.info("Database connection closed.")

if __name__ == "__main__":
    database_airconditioner_scanner()
