from class_network_client import *
def getHumidity():
    pass
def getTemperature():
    pass

def main():
    sensor = Client()
    sensor.connectToServer()
    server_data = sensor.getData()
    
    while server_data != 'CONTINUE':
        server_data = sensor.getData()
    
    humidity = getHumidity()
    temperature = getTemperature()
    sensor.sendData([humidity, temperature])