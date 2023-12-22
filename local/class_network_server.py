import socket

class Server:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 5000
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def setIp(self):
        self.user_input = input("NEW IP: ")
        if self.user_input != '':
            self.ip = self.user_input
    def setPort(self):
        self.user_input = input("NEW PORT: ")
        if self.user_input != '':
            self.port = int(self.user_input)

    def bindServer(self):
        self.server.bind((self.ip, self.port))
        print("CONNETED ESTABLISHED")
    def listenForConnection(self, amount_of_connections: int):
        self.server.listen(amount_of_connections)
        print(f"LISTENING FOR {amount_of_connections} CONNECTIONS")
    def acceptClient(self):
        client, client_address = self.server.accept()
        print("CLIENT ACCEPTED")
        return client, client_address

    """
    **********************************************************************************
    Assuming that the data is being sent to our server as a 
    list, we can use the eval() function to transform it into
    a list object from the string that is being sent.
    **********************************************************************************
    """
    def getDataAsList(self, client):
        self.client_data = client.recv(1024).decode()
        return eval(self.client_data)
    def sendData(self, client, data):
        client.sendall(data.encode())