from database_root import *
from datetime import datetime

class Airconditioner(Database):
    def __init__(self):
        super().__init__()
        self.ai_command = self.get_command_from_ai()  # Fetch and store the AI command

    def get_command_from_ai(self):
        select_query = "SELECT command FROM ai_command_table LIMIT 1;"
        self.cursor.execute(select_query)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            print("No AI command found.")
            return None

    def write_command_to_ac(self):
        if self.ai_command:
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            insert_query = "INSERT INTO air_conditioner (timestamp, command) VALUES (?, ?);"
            self.cursor.execute(insert_query, (current_timestamp, self.ai_command))
            self.database_connection.commit()
        else:
            print("No AI command to write to the AC table.")

    def close_connection(self):
        self.closeConnection()

def test():
    print("CREATING OBJECT")
    ac = Airconditioner()

if __name__ == "__main__":
    test()