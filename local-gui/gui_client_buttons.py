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
        
        self.temperature_label = ttk.Label(self, text=f"AGENT_COMMAND: {self.button_action}", font=("Arial", 14))
        self.temperature_label.pack(pady=10)

        self.client = client
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
    
    def writeQuery(self, temperature_change):
        self.insert_query = f"INSERT INTO Gui (current_profile, change_in_thermostat) VALUES ({self.DEFAULT_PROFILE}, {temperature_change});"
        return self.insert_query

    def sendQueryToDatabase(self):
        print("DETECTING CHANGE IN BUTTON COMMAND")
        self.detectButtonCommands()
        ## Sends the database the change in temperature to use.
        if (self.increase_temperature_active == True):
            self.client.sendWriteFlag()
            self.data = self.writeQuery("increase")
            self.client.sendData(self.data)
            
            ## Resets the temperature increase.
            self.increase_temperature_active = False
        elif (self.decrease_temperature_active == True):
            self.client.sendWriteFlag()
            self.data = self.writeQuery("decrease")
            self.client.sendData(self.data)

            ## Resets the temperature decrease.
            self.decrease_temperature_active = False
        else:
            self.client.sendWriteFlag()
            self.data = self.writeQuery("no change")
            self.client.sendData(self.data)

if __name__ == '__main__':
    ## Configure with custom ip/port number for the Client() object.
    client = Client()
    client.connectToServer()

    thermostat_buttons = ThermostatButton(client)
    thermostat_buttons.mainloop()