from class_network_server import *
from class_sensor import *

def main():
    server = Server()

    server.setIp()
    server.setPort()
    server.bindServer()
    server.listenForConnection(1)
    client, client_address = server.acceptClient()

    sensor_object = Sensor(None)
    while True:
        server.sendData(client, "CONTINUE")

        client_data = server.getDataAsList(client)
        while client_data == '':
            client_data = server.getDataAsList(client)
        print("CLIENT DATA CAPTURED:")
        print(f"{client_data}, {client_data[0]}, {client_data[1]}, {client_data[2]}")
        
        sensor_object.setSensorId(client_data[0])
        sensor_object.setTemperature(client_data[1])
        sensor_object.setHumidity(client_data[2])
        
        print("DATABASE_UPDATED")
        sensor_object.updateDatabase()

        client_data = ''
if __name__ == "__main__":
    main()