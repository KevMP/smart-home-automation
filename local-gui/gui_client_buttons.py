import tkinter as tk
from tkinter import ttk
from gpiozero import Button
from class_network_client import *

class SmartThermostatApp(tk.Tk):
    def __init__(self, client):
        super().__init__()
        self.INCREASE_TEMPERATURE_BUTTON = 21 ## GPIO Pin number.
        self.DECREASE_TEMPERATURE_BUTTON = 28 ## GPIO Pin number.
        self.DEFAULT_PROFILE = "default"
        
        self.title("Smart AI Thermostat")
        self.geometry("300x100")

        self.increase_temperature_active = False
        self.decrease_temperature_active = False
        
        self.temperature_label = ttk.Label(self, text=f"AGENT_COMMAND: {self.button_action}", font=("Arial", 14))
        self.temperature_label.pack(pady=10)

        self.client = client

    def detectButtonCommands(self):
        if self.INCREASE_TEMPERATURE_BUTTON.is_pressed:
            print("INCREASE BUTTON HAS BEEN PRESSED")
            self.increase_temperature_active = True

        elif self.DECREASE_TEMPERATURE_BUTTON.is_pressed:
            print("DECREASE BUTTON HAS BEEN PRESSED")
            self.decrease_temperature_active = True

        else:
            print("NO ACTION DETECTED")
    
    def writeQuery(self, temperature_change):
        self.insert_query = f"INSERT INTO Gui (current_profile, change_in_thermostat) VALUES ({self.DEFAULT_PROFILE}, {temperature_change});"
        return self.insert_query

    def sendQueryToDatabase(self):
        print("DETECTING CHANGE IN BUTTON COMMAND")
        self.getButtonAction()
        ## Sends the database the change in temperature to use.
        if (self.increase_temperature_active == True):
            self.client.sendWriteFlag()
            self.data = self.client.writeQuery("increase")
            self.client.sendData(self.data)
            
            ## Resets the temperature increase.
            self.increase_temperature_active = False
        elif (self.decrease_temperature_active == True):
            self.client.sendWriteFlag()
            self.data = self.client.writeQuery("decrease")
            self.client.sendData(self.data)

            ## Resets the temperature decrease.
            self.decrease_temperature_active = False
        else:
            self.client.sendWriteFlag()
            self.data = self.client.writeQuery("no change")
            self.client.sendData(self.data)

if __name__ == '__main__':
    client = Client()
    client.connectToServer()

    app = SmartThermostatApp(client)
    app.mainloop()