import socket
import time

class Client:
    def __init__(self, ip: str="127.0.0.1", port: int=5000):
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectToServer(self):
        self.client.connect((self.ip, self.port))
    
    def getData(self):
        return self.client.recv(1024).decode('utf-8')
    def sendData(self, data):
        self.client.sendall(data.encode('utf-8'))