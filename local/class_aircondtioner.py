from database_root import *
from datetime import datetime

class Airconditioner(Database):
    def __init__(self):
        super().__init__()
        self.command_to_ac = self.get_command_from_ai()  # Fetch and store the AI command

    def get_command_from_ai(self):
        select_query = "SELECT command_to_AC FROM Temperature_Mode ORDER BY timestamp DESC LIMIT 1;"
        self.cursor.execute(select_query)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            print("No recent command found.")
            return None

    def write_command_to_ac(self):
        if self.command_to_ac:
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            insert_query = "INSERT INTO Temperature_Mode (timestamp, command_to_AC) VALUES (?, ?);"
            self.cursor.execute(insert_query, (current_timestamp, self.command_to_ac))
            self.database_connection.commit()
        else:
            print("No command to write to the Temperature_Mode table.")

    def close_connection(self):
        self.closeConnection()

def test():
    print("CREATING OBJECT")
    ac = Airconditioner()
    print("WRITING TO DATABASE")
    ac.write_command_to_ac()
    print("CLOSING CONNECTION")
    ac.close_connection()

if __name__ == "__main__":
    test()