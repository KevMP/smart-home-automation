from class_network_server import *
from database_root import *

def main():
    AMOUNT_OF_CLIENTS = 2    

    database = Database()

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
            client_data = server.getData(connected_client)
            database.updateDatabase(client_data)

if __name__ == "__main__":
    main()