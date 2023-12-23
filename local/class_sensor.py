from database_root import *
"""
**********************************************************************************
to install the Adafruit_DHT library,
use this,

pip install Adafruit-DHT or sudo pip3 install Adafruit_DHT

if that doesn't work use this,

sudo apt-get install python3-dev python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT

Example on how to use this for the hardware side of things,

    from class_sensor import *
    import Adafruit_DHT
    import time

    SENSOR_0 = Sensor(0)
    DHT_SENSOR_0 = Adafruit_DHT.DHT11
    DHT_PIN_0 = 7

    SENSOR_1 = Sensor(1)
    DHT_SENSOR_1 = Adafruit_DHT.DHT11
    DHT_PIN_1 = 4

    SENSOR_2 = Sensor(2)
    DHT_SENSOR_2 = Adafruit_DHT.DHT11
    DHT_PIN_2 = 3

    while True:
        humidity_0, temperature_0 = Adafruit_DHT.read(DHT_SENSOR0, DHT_PIN_0)
        humidity_1, temperature_1 = Adafruit_DHT.read(DHT_SENSOR1, DHT_PIN_1)
        humidity_2, temperature_2 = Adafruit_DHT.read(DHT_SENSOR2, DHT_PIN_2)
        if (humidity_0 is not None and temperature_0 is not None):
            SENSOR_0.setHumidity(humidity_0)
            SENSOR_0.setTemperature(temperature_0)
        if (humidity_1 is not None and temperature_1 is not None):
            SENSOR_1.setHumidity(humidity_1)
            SENSOR_1.setTemperature(temperature_1)
        if (humidity_2 is not None and temperature_2 is not None):
            SENSOR_2.setHumidity(humidity_2)
            SENSOR_2.setTemperature(temperature_2)
    
information sources used,
https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/
https://github.com/adafruit/Adafruit_Python_DHT/tree/master/examples
**********************************************************************************
"""
class Sensor(Database):
    def __init__(self, id: int, sensor_pinout: int=None):
        super().__init__()
        self.sensor_id = id
        self.temperature = 0.0
        self.humidity = 0.0
        self.sensor_pinout = sensor_pinout

    def setSensorId(self, value: int):
        self.sensor_id = value
    def setTemperature(self, value: float):
        self.temperature = value
    def setHumidity(self, value: float):
        self.humidity = value

    def updateDatabase(self):
        if not self.database_connection:
            print("Cannot update database. Database connection not available.")
            return None

        self.insert_query = f"""
            INSERT INTO Sensor (id, temperature, humidity)
            VALUES ({self.sensor_id}, {self.temperature}, {self.humidity});
        """

        print("DATABASE UPDATED")
        self.cursor.execute(self.insert_query)
        self.database_connection.commit()