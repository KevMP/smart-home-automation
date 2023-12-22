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
    """
    **********************************************************************************
    The following server is going to send the client a message that allows the client
    to continue or not, after the client receives a list of data it will then move on
    and write that data.

    This is to prevent a data overflow, where one socket gets much more data leading
    to a "corruption" of sorts on the receiving data.
    **********************************************************************************
    """
    while True:
        server.sendData(client, "CONTINUE")

        client_data = server.getDataAsList(client)
        while client_data == '':
            print("GETTING CLIENT DATA")
            client_data = server.getDataAsList(client)
            print(client_data)

        sensor_object.setSensorId(client_data[0])
        sensor_object.setTemperature(client_data[1])
        sensor_object.setHumidity(client_data[2])
        
        print("DATABASE_UPDATED")
        sensor_object.updateDatabase()

        client_data = ''
if __name__ == "__main__":
    main()