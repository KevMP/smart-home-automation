from database_root import *

class Airconditioner(Database):
    def __init__(self, command_to_ac=None):
        super().__init__()
        self.command_to_ac = command_to_ac  # Initialize the command_to_ac attribute

    def get_command_from_ai(self):
        select_query = "SELECT airconditioner_command FROM TemperatureModel ORDER BY timestamp DESC LIMIT 1;"
        self.cursor.execute(select_query)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            print("No recent command found.")
            return None

    def write_command_to_ac(self):
        if self.command_to_ac is not None:  # Check if command_to_ac is not None instead of if it exists
            insert_query = "INSERT INTO Airconditioner (command) VALUES (?);"
            self.cursor.execute(insert_query, (self.command_to_ac,))
            self.database_connection.commit()
        else:
            print("No command to write to the Airconditioner table.")

    def close_connection(self):
        self.closeConnection()

def test():
    print("CREATING OBJECT")
    command = 'your_command_here'  # Replace with the actual command
    ac = Airconditioner(command)
    print("WRITING TO DATABASE")
    ac.write_command_to_ac()
    print("CLOSING CONNECTION")
    ac.close_connection()

if __name__ == "__main__":
    test()
