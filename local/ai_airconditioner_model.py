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

    def calculateFeelsLikeTemperature(self):
        """
        calculates the feels like temperature, using the
        self.averageTemperature and the self.averageHumdity,
        assigns that value to the feelsLikeTemperature.
        """
        pass

model = AirconditionerModel()
model.getAverageTemperature()
model.getAverageHumidity()
model.closeConnection()
print(model.averageTemperature)
print(model.averageHumidity)