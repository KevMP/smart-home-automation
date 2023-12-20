from class_model import *
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
        
        self.current_profile = 'DEFAULT'
        self.profile_minimum_temp = 50
        self.profile_maximum_temp = 70
    
    def getAverageTemperature(self):
        if not self.database_connection:
            print("Cannot fetch data. Database connection not available.")
            return None

        try:
            query = """
                SELECT id, AVG(temperature) as average_temperature
                FROM sensor
                ORDER BY MAX(timestamp) DESC;
            """

            result = self.cursor.execute(query).fetchone()
            if result:
                self.average_temperature = result[1]

        except sql.Error as e:
            print(f"Error fetching data: {e}")

    def getAverageHumidity(self):
        if not self.database_connection:
            print("Cannot fetch data. Database connection not available.")
            return None

        try:
            # Query to get the average humidity for each sensor id
            query = """
                SELECT id, AVG(humidity) as average_humidity
                FROM sensor
                ORDER BY MAX(timestamp) DESC;
            """

            result = self.cursor.execute(query).fetchone()
            if result:
                self.average_humidity = result[1]

        except sql.Error as e:
            print(f"Error fetching data: {e}")

    def calculateFeelsLikeTemperature(self):
        self.coefficients = [-42.379, 2.04901523, 10.14333127, -0.22475541, -6.83783e-3,
            -5.481717e-2, 1.22874e-3, 8.5282e-4, -1.99e-6]
        
        self.relative_humidity = self.average_humidity / 100.0

        self.feels_like_temperature = self.coefficients[0] + self.coefficients[1] * self.average_temperature + self.coefficients[2] * self.relative_humidity + \
                    self.coefficients[3] * self.average_temperature  * self.relative_humidity + self.coefficients[4] * self.average_temperature **2 + \
                    self.coefficients[5] * self.relative_humidity**2 + self.coefficients[6] * self.average_temperature **2 * self.relative_humidity + \
                    self.coefficients[7] * self.average_temperature  * self.relative_humidity**2 + self.coefficients[8] * self.average_temperature **2 * self.relative_humidity**2

    def getCurrentProfileFromGui(self):
        if not self.database_connection:
            print("Cannot fetch data. Database connection not available.")
            return None

        try:
            query = """
                SELECT current_profile
                FROM Gui
                ORDER BY timestamp DESC
            """

            result = self.cursor.execute(query).fetchone()
            print(f"PROFILE RESULT: {result}")
            if result:
                self.current_profile = result[0]

        except sql.Error as e:
            print(f"Error fetching profile: {e}")

    def getProfileMinimumPreferredTemperature(self):
        if not self.database_connection or not self.current_profile:
            print("Cannot fetch data. Database connection not available or current_profile not set.")
            return None

        try:
            query = """
                SELECT min_temp
                FROM Profile
                WHERE name = ?;
            """

            result = self.cursor.execute(query, (self.current_profile,)).fetchone()
            if result:
                self.profile_minimum_temp = result[0]

        except sql.Error as e:
            print(f"Error fetching profile minimum temperature: {e}")

    def getProfileMaximumPreferredTemperature(self):
        if not self.database_connection or not self.current_profile:
            print("Cannot fetch data. Database connection not available or current_profile not set.")
            return None

        try:
            query = """
                SELECT max_temp
                FROM Profile
                WHERE name = ?;
            """

            result = self.cursor.execute(query, (self.current_profile,)).fetchone()
            if result:
                self.profile_maximum_temp = result[0]

        except sql.Error as e:
            print(f"Error fetching profile maximum temperature: {e}")

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
        if not self.database_connection:
            print("Cannot write data. Database connection not available.")
            return

        try:
            query = """
                INSERT INTO TemperatureModel (airconditioner_command)
                VALUES (?);
            """

            self.cursor.execute(query, (command,))
            self.database_connection.commit()

        except sql.Error as e:
            print(f"Error writing command to database: {e}")

def test():
    model = AirconditionerModel()
    model.getAverageTemperature()
    model.getAverageHumidity()
    model.calculateFeelsLikeTemperature()
    model.getCurrentProfileFromGui()
    model.getProfileMaximumPreferredTemperature()
    model.getProfileMinimumPreferredTemperature()
    command = model.getCommandBasedOnCurrentProfile()
    command = model.getCommandBasedOnCurrentProfile()
    command = model.getCommandBasedOnCurrentProfile()
    command = model.getCommandBasedOnCurrentProfile()
    command = model.getCommandBasedOnCurrentProfile()
    command = model.getCommandBasedOnCurrentProfile()
    command = model.getCommandBasedOnCurrentProfile()
    model.writeCommandToDatabase(command)
    model.closeConnection()
    print(model.average_temperature)
    print(model.average_humidity)
    print(model.feels_like_temperature)
    print(model.current_profile)
    print(model.profile_maximum_temp)
    print(command)

def main():
    temperature_model = AirconditionerModel()
    while True:
        temperature_model.getCurrentProfileFromGui()
        temperature_model.getProfileMaximumPreferredTemperature()
        temperature_model.getProfileMinimumPreferredTemperature()

        temperature_model.getAverageTemperature()
        temperature_model.getAverageHumidity()
        temperature_model.calculateFeelsLikeTemperature()

        command = temperature_model.getCommandBasedOnCurrentProfile()
        temperature_model.writeCommandToDatabase(command)
        print(temperature_model.current_profile)

if __name__ == "__main__":
    main()