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
    


if __name__ == '__main__':
    client = Client()
    client.connectToServer()

    app = SmartThermostatApp(client)
    app.mainloop()