from class_network_client import *
import RPi.GPIO as GPIO

def setupGPIO(relay_pin):
    # Set up GPIO using BCM numbering
    GPIO.setmode(GPIO.BCM)
    # Set the relay pin as output
    GPIO.setup(relay_pin, GPIO.OUT)

def writeCommandToAirconditioner(command, relay_pin):
    # This function writes a command to the air conditioner via relay.
    if command == "increase":
        GPIO.output(relay_pin, GPIO.HIGH)  # Turn relay on
    elif command == "decrease":
        GPIO.output(relay_pin, GPIO.LOW)  # Turn relay off

def getCommandFromDatabase():
    query = """
            SELECT command 
            FROM Airconditioner 
            ORDER BY timestamp DESC 
            LIMIT 1;
            """
    return query

def main():
    RELAY_PIN = 17
    setupGPIO(RELAY_PIN)

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

        ## Command gets sent out to the relay based on database data.
        writeCommandToAirconditioner(command, RELAY_PIN)