from class_network_client import *
import RPi.GPIO as GPIO

def writeCommandToAirconditioner(command):
    ## This function writes a command to the air conditioner.
    relay_address = 0xF1 ## change to whatever the relay Address is set to.
    if command == "increase":
        on  = 10000000 ## Binary value of 1 example.
        write_data_byte_to_relay(on, relay_address)
    elif command == "decrease":
        off = 00000000 ## Binary value of 0 example.
        write_data_byte_to_relay(off, relay_address)

def isAirconditionerOn():
    ## This function should return a true/false based
    ## on if the airconditioner is activated or not.
    airconditioner_status = False
    if airconditioner_status == True:
        return True
    else:
        return False

def getCommandFromDatabase():
    query = """
            SELECT command 
            FROM Airconditioner 
            ORDER BY timestamp DESC 
            LIMIT 1;
            """
    return query

def main():
    client = Client("127.0.0.1", 5000) ## Configure to correct addresses.
    client.connectToServer()
    while True:
        ## Tells the client handler to prepare for our communication.
        client.sendReadFlag()
        client.sendData(getCommandFromDatabase())

        raw_command = client.getData()
        ## Parses to a string.
        command = eval(raw_command)
        command = command[0][0]

        ## Command gets sent out to the relay based on client data.
        writeCommandToAirconditioner(command)