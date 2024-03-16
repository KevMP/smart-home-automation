from class_network_server import *
from database_root import *
import time

def acceptClients(AMOUNT_OF_CLIENTS=1, server=None):
    client_counter = 0
    connected_clients = []
    server.listenForConnection(AMOUNT_OF_CLIENTS)

    for connected_client in range(AMOUNT_OF_CLIENTS):
        print(f"Clients connected {client_counter}/{AMOUNT_OF_CLIENTS}")
        client, client_address = server.acceptClient()
        connected_clients.append(client)

        client_counter += 1
    print("ALL CLIENTS ACCEPTED, STARTING MAIN LOOP")
    time.sleep(1)
    return connected_clients

def main():
    database = Database()

    server = Server()
    server.bindServer()
    connected_clients = acceptClients(1, server)
    """
    To prevent data overflow from drowning our socket,
    we are sending each client a "CONTINUE" signal that
    allows them to send data.

    Which then prompts the client to send us a WRITE or READ
    flag.
    """
    while True:
        for connected_client in connected_clients:
            """The following sequence is based on our network client
               flag structure. i.e.

                def sendWriteFlag(self, client):
                    self.waitForServerContinueFlag(client)
                    self.sendData("WRITE")
                    self.waitForServerContinueFlag(client)
                def sendReadFlag(self, client):
                    self.waitForServerContinueFlag(client)
                    self.sendData("READ")
                    self.waitForServerContinueFlag(client)
            """
            server.sendData(connected_client, "CONTINUE")
            client_flag = server.getData(connected_client)
            server.sendData(connected_client, "CONTINUE")

            client_query = server.getData(connected_client)
            if client_flag == "WRITE":
                database.writeToDatabase(client_query)
            elif client_flag == "READ":
                database_data = database.getFromDatabase(client_query)
                server.sendData(connected_client, database_data)
            client_query = ''
            client_flag = ''
            ## time.sleep(1)

if __name__ == "__main__":
    main()