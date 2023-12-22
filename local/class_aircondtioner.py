from database_root import *

class Airconditioner(Database):
    def __init__(self):
        super().__init__()
        self.command_to_ac = ""  # Initialize command_to_ac to an empty string

    def get_command_from_ai(self):
        select_query = "SELECT airconditioner_command FROM TemperatureModel ORDER BY timestamp DESC LIMIT 1;"
        self.cursor.execute(select_query)
        result = self.cursor.fetchone()
        if result:
            self.command_to_ac = result[0]  # Set command_to_ac with the command from AI
            return self.command_to_ac
        else:
            print("No recent command found.")
            return None

    def write_command_to_ac(self):
        if self.command_to_ac:  # Check if command_to_ac has been set by get_command_from_ai
            insert_query = "INSERT INTO Airconditioner (command) VALUES (?);"
            self.cursor.execute(insert_query, (self.command_to_ac,))
            self.database_connection.commit()
        else:
            print("No command to write to the Airconditioner table.")

    def close_connection(self):
        self.closeConnection()

def test():
    print("CREATING OBJECT")
    ac = Airconditioner()
    print("GETTING COMMAND FROM AI")
    ac.get_command_from_ai()  # This will attempt to get the command and set it
    print("WRITING TO DATABASE")
    ac.write_command_to_ac()  # This will write the command if it was successfully retrieved
    print("CLOSING CONNECTION")
    ac.close_connection()

if __name__ == "__main__":
    pass