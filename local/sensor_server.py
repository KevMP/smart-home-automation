from class_sensor import *
from class_network_server import *

def main():
    server = Server()

    server.setIp()
    server.setPort()
    server.bindServer()
    server.listenForConnection(1)
    client, client_address = server.acceptClient()

    while True:
        server.sendData(client, "CONTINUE")
        client_data = server.getDataAsList(client)
        while client_data == '':
            client_data = server.getDataAsList(client)