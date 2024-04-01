import tkinter as tk
from tkinter import ttk
from gpiozero import Button
from class_network_client import *

class ThermostatButton(tk.Tk):
    def __init__(self, client):
        super().__init__()
        self.INCREASE_TEMPERATURE_BUTTON = Button(6) ## GPIO Pin number.
        self.DECREASE_TEMPERATURE_BUTTON = Button(5) ## GPIO Pin number.
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
        print("DETECTING CHANGE IN BUTTONS")

        if self.INCREASE_TEMPERATURE_BUTTON.is_pressed:
            print("INCREASE BUTTON HAS BEEN PRESSED")
            self.increase_temperature_active = True
            self.button_action = "increasing"

        elif self.DECREASE_TEMPERATURE_BUTTON.is_pressed:
            print("DECREASE BUTTON HAS BEEN PRESSED")
            self.decrease_temperature_active = True
            self.button_action = "decreasing"

        else:
            print("NO CHANGE DETECTED")
            self.button_action = "no change detected"
        
        self.agent_command.config(text=f"AGENT_COMMAND: {self.button_action}")

    def updateGuiTable(self, temperature_change):
        self.insert_query = f"INSERT INTO Gui (current_profile, change_in_thermostat) VALUES ('{self.DEFAULT_PROFILE}', '{temperature_change}');"
        return self.insert_query
    
    def updateProfilePreferences(self, temperature_change):
        if (temperature_change == "increase"):
            ## Increases the min_temp and max_temp by one.
            self.increase_preferred_temperature_range = f"""
                UPDATE Profile
                SET min_temp = min_temp + 1,
                    max_temp = max+temp + 1
                WHERE name = '{self.DEFAULT_PROFILE}';
                """
        elif (temperature_change == "decrease"):
            ## Decreases the min_temp and max_temp by one.
            self.decrease_preferred_temperature_range = f"""
                UPDATE Profile
                SET min_temp = min_temp - 1,
                    max_temp = max+temp - 1
                WHERE name = '{self.DEFAULT_PROFILE}';
                """
        else:
            return ""
    
    def sendQueryToDatabase(self):
        self.detectButtonCommands()

        print("SETTING INITIAL TEMPERATURE CHANGE VALUE TO no change")
        self.temperature_change = "no change"
        
        if (self.increase_temperature_active == True):
            self.temperature_change = "increase"
            self.increase_temperature_active = False
        elif (self.decrease_temperature_active == True):
            self.temperature_change = "decrease"
            self.decrease_temperature_active = False
        
        client.sendWriteFlag()
        ## Sends the database the change in temperature to use.
        self.data = self.updateGuiTable(self.temperature_change)
        client.sendData(self.data)

        ## Updates the profile preferences.
        self.data = self.updateProfilePreferences(self.temperature_change)
        if self.data != "":
            client.sendWriteFlag()
            client.sendData(self.data)
        
        self.after(1, self.sendQueryToDatabase)

if __name__ == '__main__':
    ## Configure with custom ip/port number for the Client() object.
    client = Client("192.168.0.111", 5000)
    client.connectToServer()

    thermostat_buttons = ThermostatButton(client)
    thermostat_buttons.mainloop()