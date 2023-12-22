from class_network_client import *
from class_sensor import *

def getTemperature():
    pass
def getHumidity():
    pass

def sensor(identification_number):
    SENSOR = Sensor(identification_number)
    SENSOR.setHumidity(getHumidity())

def main():
    sensor = Client()
    sensor.connectToServer()
    server_data = sensor.getData()

    while True:
        while server_data != "CONTINUE":
            server_data = sensor.getData()
        server_data = ''

        temperature = getTemperature()
        humidity = getHumidity()
        sensor.sendData([identification_number, temperature, humidity])