class Airconditioner():
    def __init__(self, id):
        self.command_to_ac = "do_nothing"
        self.id = id

    def getCommandFromModel(self):
        return "SELECT airconditioner_command FROM TemperatureModel ORDER BY timestamp DESC LIMIT 1;"
    def writeCommandToTable(self, command):
        return f"INSERT INTO Airconditioner (id, command) VALUES ({self.id},'{command}');"