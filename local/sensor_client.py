from class_network_client import *
from class_sensor import *

def getSensorData():
    return 10, 12

def main():
    sensor = Sensor(0)
    NUMBER_OF_OPERATIONS = 1

    client = Client()
    client.connectToServer()
    while True:
        client.waitForServerContinueFlag()
        client.sendData("WRITE")
        
        client.waitForServerContinueFlag
        humidity, temperature = getSensorData()
        sensor.setHumidity(humidity)
        sensor.setTemperature(temperature)
        sensor_query = sensor.createSensorQuery()
        client.sendData(sensor_query)

if __name__ == "__main__":
    main()