from class_model import *
from class_network_client import *
import random

class AirconditionerModel(Model):
    def __init__(self):
        super().__init__()
        self.airconditioner_model = Model()
        self.airconditioner_model.addDecision("raise")
        self.airconditioner_model.addDecision("lower")
        self.airconditioner_model.addDecision("do_nothing")

        self.average_temperature = 0.0
        self.average_humidity = 0.0
        self.feels_like_temperature = 0.0
        
        self.current_profile = "default"
        self.profile_minimum_temp = 50
        self.profile_maximum_temp = 70

    def getCurrentProfileFromGui(self):
        return "SELECT current_profile FROM Gui ORDER BY timestamp DESC;"
    def getProfileMaximumPreferredTemperature(self):
        return f"SELECT max_temp FROM Profile WHERE name = '{self.current_profile}';"
    def getProfileMinimumPreferredTemperature(self):
        return f"SELECT min_temp FROM Profile WHERE name = '{self.current_profile}';"

    def getAverageTemperature(self):
        return "SELECT AVG(temperature) FROM sensor WHERE temperature IS NOT NULL AND (id, timestamp) IN (SELECT id, MAX(timestamp) as max_timestamp FROM sensor WHERE temperature IS NOT NULL GROUP BY id);"
    def getAverageHumidity(self):
        return "SELECT AVG(humidity) FROM sensor WHERE humidity IS NOT NULL AND (id, timestamp) IN (SELECT id, MAX(timestamp) as max_timestamp FROM sensor WHERE humidity IS NOT NULL GROUP BY id);"

    def calculateFeelsLikeTemperature(self):
        self.coefficients = [-42.379, 2.04901523, 10.14333127, -0.22475541, -6.83783e-3,
            -5.481717e-2, 1.22874e-3, 8.5282e-4, -1.99e-6]
        
        self.relative_humidity = self.average_humidity / 100.0

        self.feels_like_temperature = self.coefficients[0] + self.coefficients[1] * self.average_temperature + self.coefficients[2] * self.relative_humidity + \
                    self.coefficients[3] * self.average_temperature  * self.relative_humidity + self.coefficients[4] * self.average_temperature **2 + \
                    self.coefficients[5] * self.relative_humidity**2 + self.coefficients[6] * self.average_temperature **2 * self.relative_humidity + \
                    self.coefficients[7] * self.average_temperature  * self.relative_humidity**2 + self.coefficients[8] * self.average_temperature **2 * self.relative_humidity**2

    """
    **********************************************************************************
    The following will make a command to the airconditioner that will later pass it
    to a function that writes it to the database.

    the logic is as follows,
        IF REAL TEMPERATURE IS INSIDE PREFERRENCES RANGE
            IF COMMAND TO AIR CONDITIONER IS NOT DO NOTHING
                PUNISH
        IF REAL TEMPERATURE IS LESS THAN PREFERRED MINIMUM
            IF COMMAND TO AIR CONDITIONER IS NOT RAISE
                PUNISH
        IF REAL TEMPERATURE IS MORE THAN PREFERRED MAXIMUM
            IF COMMAND TO AIR CONDITIONER IS NOT LOWER
                PUNISH
        ELSE
            REWARD
    
    punishing the ai means randomly swapping out a action in its action_matrix,
    rewarding it on the other hand means randomly swapping out a action with its
    current output action
    **********************************************************************************
    """
    def getCommandBasedOnCurrentProfile(self):
        self.command_to_airconditioner = random.choice(self.airconditioner_model.action_matrix)
        self.random_action_matrix_index = random.randint(0, 2)
        self.random_decision_tree_index = random.randint(0, 2)
        if (self.feels_like_temperature >= self.profile_minimum_temp) and (self.feels_like_temperature <= self.profile_maximum_temp):
            if self.command_to_airconditioner != 'do_nothing':
                self.airconditioner_model.action_matrix[self.random_action_matrix_index] = self.airconditioner_model.decision_tree[self.random_decision_tree_index]
        elif (self.feels_like_temperature < self.profile_minimum_temp):
            if self.command_to_airconditioner != 'raise':
                self.airconditioner_model.action_matrix[self.random_action_matrix_index] = self.airconditioner_model.decision_tree[self.random_decision_tree_index]
        elif (self.feels_like_temperature > self.profile_maximum_temp):
            if self.command_to_airconditioner != 'lower':
                self.airconditioner_model.action_matrix[self.random_action_matrix_index] = self.airconditioner_model.decision_tree[self.random_decision_tree_index]
        else:
            self.airconditioner_model.action_matrix[self.random_action_matrix_index] = self.command_to_airconditioner
        return self.command_to_airconditioner
    
    def writeCommandToDatabase(self, command: str):
            return f"INSERT INTO TemperatureModel (airconditioner_command) VALUES ('{command}');"

def main():
    temperature_model = AirconditionerModel()
    client = Client()
    client.connectToServer()
    while True:
        ## Gets the current profile from the Gui table.
        client.waitForServerContinueFlag(client)
        client.sendReadFlag(client)

        client.sendData(temperature_model.getCurrentProfileFromGui())
        current_profile = client.getData()
        if current_profile != "None":
            temperature_model.current_profile = current_profile
        
        ## Gets the profiles maximum preferred temperature
        client.waitForServerContinueFlag(client)
        client.sendReadFlag(client)

        client.sendData(temperature_model.getProfileMaximumPreferredTemperature())
        ## Since the data is returned as a string in a tuple format "(data,)"
        ## we need to convert it to a tuple using the eval function, and then
        ## select the first index where our temperature is being stored.
        tuple_maximum_temperature = eval(client.getData())
        temperature_model.profile_maximum_temp = tuple_maximum_temperature[0]

        ## Gets the minimum preferred temperature
        client.waitForServerContinueFlag(client)
        client.sendReadFlag(client)
        
        client.sendData(temperature_model.getProfileMinimumPreferredTemperature())
        tuple_minimum_temperature = eval(client.getData())
        temperature_model.profile_minimum_temp = tuple_minimum_temperature[0]
        
        ## Gets the average temperature
        client.waitForServerContinueFlag(client)
        client.sendReadFlag(client)
        
        client.sendData(temperature_model.getAverageTemperature())
        tuple_average_temperature = eval(client.getData())
        temperature_model.average_temperature = tuple_average_temperature[0]
        
        ## Gets the average humidity
        client.waitForServerContinueFlag(client)
        client.sendReadFlag(client)
        
        client.sendData(temperature_model.getAverageHumidity())
        tuple_average_humidity = eval(client.getData())
        temperature_model.average_humidity = tuple_average_humidity[0]
        
        ## Writes the command to the database
        client.waitForServerContinueFlag(client)
        client.sendWriteFlag(client)
        
        command = temperature_model.getCommandBasedOnCurrentProfile()
        client.sendData(temperature_model.writeCommandToDatabase(command))
if __name__ == "__main__":
    main()