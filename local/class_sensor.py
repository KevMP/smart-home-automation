from database_root import *
"""
**********************************************************************************
Example on how to use this for the hardware side of things,

    from class_sensor import *
    import Adafruit_DHT
    import time

    SENSOR_0 = Sensor(0)
    DHT_SENSOR_0 = Adafruit_DHT.DHT11
    DHT_GPIO_PIN_0 = 7

    SENSOR_1 = Sensor(1)
    DHT_SENSOR_1 = Adafruit_DHT.DHT11
    DHT_GPIO_PIN_1 = 4

    SENSOR_2 = Sensor(2)
    DHT_SENSOR_2 = Adafruit_DHT.DHT11
    DHT_GPIO_PIN_2 = 3

    while True:
        humidity_0, temperature_0 = Adafruit_DHT.read(DHT_SENSOR0, DHT_PIN)
        humidity_1, temperature_1 = Adafruit_DHT.read(DHT_SENSOR1, DHT_PIN)
        humidity_2, temperature_2 = Adafruit_DHT.read(DHT_SENSOR2, DHT_PIN)
        if (humidity_0 is not None and temperature_0 is not None):
            SENSOR_0.setHumidity(humidity_0)
            SENSOR_0.setTemperature(temperature_0)
        if (humidity_1 is not None and temperature_1 is not None):
            SENSOR_1.setHumidity(humidity_1)
            SENSOR_1.setTemperature(temperature_1)
        if (humidity_2 is not None and temperature_2 is not None):
            SENSOR_2.setHumidity(humidity_2)
            SENSOR_2.setTemperature(temperature_2)
            
**********************************************************************************
"""
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

    def updateDatabase(self):
        if not self.database_connection:
            print("Cannot update database. Database connection not available.")
            return None
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

        self.cursor.execute(insert_query, (self.sensor_id, self.temperature, self.humidity))
        self.database_connection.commit()