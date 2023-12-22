import socket

class Client:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 5000
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def setIp(self):
        self.ip = input("NEW IP: ")
    def setPort(self):
        self.port = int(input("NEW PORT: "))

    def connectToServer(self):
        self.client.connect((self.ip, self.port))
        print("CONNETED ESTABLISHED")
    
    def getData(self):
        return self.client.recv(1024).decode()
    def sendData(self, data):
        self.client.sendall(data)