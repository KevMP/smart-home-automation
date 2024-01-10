from class_network_client import *
from class_sensor import *

def getSensorData():
    return 10, 12

def main():
    sensor = Sensor(0)

    client = Client() ## Configure the IPv4 address and PORT number to the Client Handler.
    client.connectToServer()
    while True:
        client.sendWriteFlag(client)
        
        humidity, temperature = getSensorData()
        sensor.setHumidity(humidity)
        sensor.setTemperature(temperature)
        sensor_query = sensor.createSensorQuery()

        client.sendData(sensor_query)

if __name__ == "__main__":
    main()