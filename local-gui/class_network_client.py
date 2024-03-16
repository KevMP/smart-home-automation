import socket

class Client:
    def __init__(self, ip: str="127.0.0.1", port: int=5000):
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectToServer(self):
        self.client.connect((self.ip, self.port))
    """
    The following function is meant to serve as a
    buffer for our client/server communication,
    this is to prevent the client from bombarding
    the server with data.

    it will await a continue flag from our server,
    and until that happens, our client won't be sending
    any data.
    """
    def waitForServerContinueFlag(self):
        self.client_data = ""
        while self.client_data != "CONTINUE":
            print("Waiting for server...")
            self.client_data = self.getData()
        print("CONTINUE CAPTURED")

    def getData(self):
        return self.client.recv(1024).decode('utf-8')
    def sendData(self, data):
        self.client.sendall(data.encode('utf-8'))
    def sendWriteFlag(self):
        self.waitForServerContinueFlag()
        self.sendData("WRITE")
        self.waitForServerContinueFlag()
    def sendReadFlag(self):
        self.waitForServerContinueFlag()
        self.sendData("READ")
        self.waitForServerContinueFlag()