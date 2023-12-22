from class_network_client import *
from class_sensor import *
## import Adafruit_DHT
def getSensorData(gpio_pin):
    """
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PINOUT = gpio_pin
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PINOUT)
    return humidity, temperature
    """
    pass

def sensorConstructor(identification_number: int, gpio_pin: int):
    humidity, temperature = getSensorData(gpio_pin)
    while humidity is not None and temperature is not None:
        sensor_object = Sensor(identification_number)
        sensor_object.setHumidity(humidity)
        sensor_object.setTemperature(temperature)
        return sensor_object

def main():
    client = Client()
    client.connectToServer()
    server_data = client.getData()

    sensor0 = sensorConstructor(0, 8)
    sensor1 = sensorConstructor(1, 3)
    sensor2 = sensorConstructor(2, 7)
    list_of_sensors = [sensor0, sensor1, sensor2]
    """
    **********************************************************************************
    The following is going to be sending data from multiple
    sensors, the list above is so that we can expand how many
    sensors we are sending to the database.

    However sensor specific data still needs to be built, currently
    it is only capturing sensor data from one sensor, or however
    the getTemperature and getHumidity functions are made.
    **********************************************************************************
    """
    while True:
        for sensor in list_of_sensors:
            while server_data != "CONTINUE":
                server_data = client.getData()
            server_data = ''

            client.sendData(f"[{sensor.sensor_id}, {sensor.temperature}, {sensor.humidity}]")
            print("DATA SENT")

if __name__ == "__main__":
    main()