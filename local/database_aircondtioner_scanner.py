from class_aircondtioner import *
from class_network_client import *

def database_airconditioner_scanner():
    airconditioner_object = Airconditioner(0)
    client = Client()
    client.connectToServer()

    while True:
        client.sendReadFlag(client)
        print("READING DATA")
        client.sendData(airconditioner_object.getCommandFromModel())
        command = eval(client.getData())
        command = command[0][0]
        
        client.sendWriteFlag(client)
        print("SENDING DATA")
        client.sendData(airconditioner_object.writeCommandToTable(command))
        print(f"COMMAND: {command} WRITTEN TO THE AIRCONDITIONER TABLE")

if __name__ == "__main__":
    database_airconditioner_scanner()
