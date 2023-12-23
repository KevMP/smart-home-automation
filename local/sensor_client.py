from class_network_client import *
from class_sensor import *
def getSensorData():
    return 10, 12
def waitForServer(client):
    client_data = client.getData()
    while client_data != "CONTINUE":
        client_data = client.getData()
    print("CONTINUE CAPTURED")

def main():
    client = Client()
    client.connectToServer()
    while True:
        waitForServer(client)
        client.sendData("[0, 10, 12]")

if __name__ == "__main__":
    main()