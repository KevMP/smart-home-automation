from database_root import *
from datetime import datetime

class Airconditioner(Database):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.ai_command = self.get_command_from_ai()

    def get_command_from_ai(self):
        # Fetch the AI command from the ai_command_table using the air conditioner's name
        # The exact table name and column name should match your database schema
        select_query = "SELECT command FROM ai_command_table WHERE ac_name = ?;"
        self.cursor.execute(select_query, (self.name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            print(f"No AI command found for the air conditioner named {self.name}.")
            return None

    def write_command_to_ac(self):
        # Insert the AI command into the air_conditioner table with the current timestamp
        if self.ai_command:
            # Get the current date and time in the format for a SQL timestamp
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            insert_query = "INSERT INTO air_conditioner (timestamp, command) VALUES (?, ?);"
            self.cursor.execute(insert_query, (current_timestamp, self.ai_command))
            self.database_connection.commit()
        else:
            print("No AI command to write to the AC table.")
    
    def __del__(self):
        # Ensure the database connection is closed when the object is deleted
        self.closeConnection()
