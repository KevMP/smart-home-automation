from class_model import *

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
        self.current_profile = ''
    
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


    """
    The following calculates the feels like temperature, so that the Ai can use that as a
    reference point in adjusting the air conditioner.
    """
    def calculateFeelsLikeTemperature(self):
        self.coefficients = [-42.379, 2.04901523, 10.14333127, -0.22475541, -6.83783e-3,
            -5.481717e-2, 1.22874e-3, 8.5282e-4, -1.99e-6]
        
        self.relative_humidity = self.average_humidity / 100.0

        self.feels_like_temperature = self.coefficients[0] + self.coefficients[1] * self.average_temperature + self.coefficients[2] * self.relative_humidity + \
                    self.coefficients[3] * self.average_temperature  * self.relative_humidity + self.coefficients[4] * self.average_temperature **2 + \
                    self.coefficients[5] * self.relative_humidity**2 + self.coefficients[6] * self.average_temperature **2 * self.relative_humidity + \
                    self.coefficients[7] * self.average_temperature  * self.relative_humidity**2 + self.coefficients[8] * self.average_temperature **2 * self.relative_humidity**2

    def getProfile(self):
        pass
    def makeDecisionBasedOnCurrentProfile(self):
        pass

model = AirconditionerModel()
model.getAverageTemperature()
model.getAverageHumidity()
model.closeConnection()
print(model.average_temperature)
print(model.average_humidity)
model.calculateFeelsLikeTemperature()
print(model.feels_like_temperature)