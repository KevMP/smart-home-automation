from database_root import *
from datetime import datetime

class Sensor(Database):
    def __init__(self, id: int):
        super().__init__()
        self.sensor_id = id
        self.temperature = 0.0
        self.humidity = 0.0

    def setTemperature(self, value: float):
        self.temperature = value
    def setHumidity(self, value: float):
        self.humidity = value

    def getSensorIdentification(self):
        return self.sensor_id
    def getTemperature(self):
        return self.temperature
    def getHumidity(self):
        return self.humidity

    def updateDatabase(self):
        if not self.database_connection:
            print("Cannot update database. Database connection not available.")
            return
        """
        **********************************************************************************
        The insert_query below will insert new sensor data depending on the timestamp and
        which sensor it is. (More on this when we get to the hardware GPIO part of things)
        **********************************************************************************
        """
        insert_query = """
            INSERT INTO Sensor (id, temperature, humidity)
            VALUES (?, ?, ?);
        """

        self.cursor.execute(insert_query, (self.getSensorIdentification(), self.getTemperature(), self.getHumidity()))
        self.database_connection.commit()

        self.closeConnection()