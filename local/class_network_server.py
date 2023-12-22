import socket

class Server:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 5000
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def setIp(self):
        self.ip = input("NEW IP: ")
    def setPort(self):
        self.port = int(input("NEW PORT: "))

    def bindServer(self):
        self.server.bind((self.ip, self.port))
        print("CONNETED ESTABLISHED")
    def listenForConnection(self, amount_of_connections: int):
        self.server.listen(amount_of_connections)
    def acceptClient(self):
        client, client_address = self.server.accept()
        return client, client_address

    def getData(self):
        return self.server.recv(1024).decode()
    def sendData(self, data):
        self.server.sendall(data)