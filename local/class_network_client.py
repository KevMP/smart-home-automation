import socket

class Client:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 5000
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def setIp(self):
        self.user_input = input("NEW IP: ")
        if self.user_input != '':
            self.ip = self.user_input
    def setPort(self):
        self.user_input = input("NEW PORT: ")
        if self.user_input != '':
            self.port = int(self.user_input)

    def connectToServer(self):
        self.client.connect((self.ip, self.port))
        print("CONNETED ESTABLISHED")
    
    def getData(self):
        return self.client.recv(1024).decode('utf-8')
    def sendData(self, data):
        self.client.sendall(data.encode('utf-8'))