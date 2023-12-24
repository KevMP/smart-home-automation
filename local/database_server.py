from class_network_server import *
from database_root import *
import time

def main():
    AMOUNT_OF_CLIENTS = 3

    database = Database()

    server = Server()
    server.bindServer()
    server.listenForConnection(AMOUNT_OF_CLIENTS)
    """
    Our server waits for every available client to connect,
    to add more clients, simply change the constant value of
    the AMOUNT_OF_CLIENTS.

    This is so that we can use a round-robin algorithm to
    allow for each client to send/receive data in a sequential
    format.
    """
    connected_clients = []
    for connected_client in range(AMOUNT_OF_CLIENTS):
        client, client_address = server.acceptClient()
        connected_clients.append(client)
    """
    To prevent data overflow from drowning our socket,
    we are sending each client a "CONTINUE" signal that
    allows them to send data.
    """
    while True:
        for connected_client in connected_clients:
            server.sendData(connected_client, "CONTINUE")
            client_data = server.getData(connected_client)
            if client_data == "WRITE":
                server.sendData(connected_client, "CONTINUE")
                client_data = server.getData(connected_client)
                database.writeToDatabase(client_data)
            elif client_data == "READ":
                server.sendData(connected_client, "CONTINUE")
                client_data = server.getData(connected_client)
                server_data = database.getFromDatabase(client_data)
                server.sendData(connected_client, server_data)
            client_data = ''
            ## time.sleep(1)

if __name__ == "__main__":
    main()