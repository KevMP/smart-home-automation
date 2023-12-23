from class_network_server import *
from class_sensor import *
import time

def main():
    AMOUNT_OF_CLIENTS = 2    
    sensor_object = Sensor(0)

    server = Server()
    server.bindServer()
    server.listenForConnection(AMOUNT_OF_CLIENTS)

    connected_clients = []
    for connected_client in range(AMOUNT_OF_CLIENTS):
        client, client_address = server.acceptClient()
        connected_clients.append(client)
    while True:
        for connected_client in connected_clients:
            server.sendData(connected_client, "CONTINUE")
            client_data = server.getDataAsList(connected_client)
            sensor_object.setSensorId(client_data[0])
            sensor_object.setHumidity(client_data[1])
            sensor_object.setTemperature(client_data[2])
            sensor_object.updateDatabase()

if __name__ == "__main__":
    main()