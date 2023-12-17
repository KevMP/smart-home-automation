from class_model import *

class AirconditionerModel(Model):
    def __init__(self):
        super().__init__()
        self.airconditionerModel = Model()
        self.airconditionerModel.addDecision("raise")
        self.airconditionerModel.addDecision("lower")
        self.airconditionerModel.addDecision("do_nothing")

        self.averageTemperature = 0.0
        self.averageHumidity = 0.0
        self.feelsLikeTemperature = 0.0
    
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
                self.averageTemperature = result[1]

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
                self.averageHumidity = result[1]

        except sql.Error as e:
            print(f"Error fetching data: {e}")


    """
    The following calculates the feels like temperature, so that the Ai can use that as a
    reference point in adjusting the air conditioner.
    """
    def calculateFeelsLikeTemperature(self):
        self.coefficients = [-42.379, 2.04901523, 10.14333127, -0.22475541, -6.83783e-3,
            -5.481717e-2, 1.22874e-3, 8.5282e-4, -1.99e-6]
        
        self.relative_humidity = self.averageHumidity / 100.0

        self.feelsLikeTemperature = self.coefficients[0] + self.coefficients[1] * self.averageTemperature + self.coefficients[2] * self.relative_humidity + \
                    self.coefficients[3] * self.averageTemperature  * self.relative_humidity + self.coefficients[4] * self.averageTemperature **2 + \
                    self.coefficients[5] * self.relative_humidity**2 + self.coefficients[6] * self.averageTemperature **2 * self.relative_humidity + \
                    self.coefficients[7] * self.averageTemperature  * self.relative_humidity**2 + self.coefficients[8] * self.averageTemperature **2 * self.relative_humidity**2

model = AirconditionerModel()
model.getAverageTemperature()
model.getAverageHumidity()
model.closeConnection()
print(model.averageTemperature)
print(model.averageHumidity)
model.calculateFeelsLikeTemperature()
print(model.feelsLikeTemperature)