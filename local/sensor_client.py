from class_network_client import *
from class_sensor import *
import Adafruit_DHT


def getSensorData(DHT_SENSOR, DHT_PIN: int):
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return humidity, temperature

def main():
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4 ## The GPIO pin
    sensor = Sensor(0)

    client = Client() ## Configure the IPv4 address and PORT number to the Client Handler.
    client.connectToServer()
    while True:
        client.sendWriteFlag(client)
        
        humidity, temperature = getSensorData(DHT_SENSOR, DHT_PIN)
        sensor.setHumidity(humidity)
        sensor.setTemperature(temperature)
        sensor_query = sensor.createSensorQuery()

        client.sendData(sensor_query)

if __name__ == "__main__":
    main()