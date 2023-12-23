import socket

class Server:
    def __init__(self, ip: str="127.0.0.1", port: int=5000):
        self.ip = ip
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def setIp(self):
        self.user_input = input("NEW IP: ")
        if self.user_input != '':
            self.ip = self.user_input

    def bindServer(self):
        self.server.bind((self.ip, self.port))
        print("CONNECTION ESTABLISHED")
    def listenForConnection(self, amount_of_connections: int):
        self.server.listen(amount_of_connections)
        print(f"LISTENING FOR {amount_of_connections} CONNECTIONS")
    def acceptClient(self):
        client, client_address = self.server.accept()
        print("CLIENT ACCEPTED")
        return client, client_address

    def getData(self, client):
        self.client_data = client.recv(1024).decode()
        return self.client_data
    
    def sendData(self, client, data):
        client.sendall(data.encode())