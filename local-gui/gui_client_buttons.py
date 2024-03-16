import tkinter as tk
from tkinter import ttk
from gpiozero import Button
from class_network_client import *

class ThermostatButton(tk.Tk):
    def __init__(self, client):
        super().__init__()
        self.INCREASE_TEMPERATURE_BUTTON = Button(26) ## GPIO Pin number.
        self.DECREASE_TEMPERATURE_BUTTON = Button(16) ## GPIO Pin number.
        self.DEFAULT_PROFILE = "default"
        
        self.title("Smart AI Thermostat")
        self.geometry("300x100")

        self.increase_temperature_active = False
        self.decrease_temperature_active = False
        self.button_action = ""
        
        self.agent_command = ttk.Label(self, text=f"AGENT_COMMAND: {self.button_action}", font=("Arial", 14))
        self.agent_command.pack(pady=10)

        self.sendQueryToDatabase()

    def detectButtonCommands(self):
        if self.INCREASE_TEMPERATURE_BUTTON.is_pressed:
            print("INCREASE BUTTON HAS BEEN PRESSED")
            self.increase_temperature_active = True
            self.button_action = "increasing"

        elif self.DECREASE_TEMPERATURE_BUTTON.is_pressed:
            print("DECREASE BUTTON HAS BEEN PRESSED")
            self.decrease_temperature_active = True
            self.button_action = "decreasing"

        else:
            print("NO ACTION DETECTED")
            self.button_action = "no action detected"
        
        self.agent_command.config(text=f"AGENT_COMMAND: {self.button_action}")

    
    def writeQuery(self, temperature_change):
        self.insert_query = f"INSERT INTO Gui (current_profile, change_in_thermostat) VALUES ('{self.DEFAULT_PROFILE}', '{temperature_change}');"
        return self.insert_query

    def sendQueryToDatabase(self):
        print("DETECTING CHANGE IN BUTTON COMMAND")
        self.detectButtonCommands()
        self.temperature_change = "no change"
        
        if (self.increase_temperature_active == True):
            self.temperature_change = "increase"
        elif (self.decrease_temperature_active == True):
            self.temperature_change = "decrease"
        
        client.sendWriteFlag()
        ## Sends the database the change in temperature to use.
        self.data = self.writeQuery(self.temperature_change)
        client.sendData(self.data)

        self.increase_temperature_active = False
        self.decrease_temperature_active = False

if __name__ == '__main__':
    ## Configure with custom ip/port number for the Client() object.
    client = Client()
    client.connectToServer()

    thermostat_buttons = ThermostatButton(client)
    thermostat_buttons.mainloop()