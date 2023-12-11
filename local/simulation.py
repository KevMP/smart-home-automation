import threading
from database import Database
from controller import Controller
import time
import random
import tkinter as tk
from tkinter import Label

class AiModel:
    def __init__(self):
        self.profile = 0
        self.min = 90
        self.max = 120
        self.actionMatrix = [0, 0, 0]

    def setProfile(self):
        self.profile = Database().getCurrentProfile()
        self.min = Database().getMinimumPreferredTemperature(self.profile)
        self.max = Database().getMaximumPreferredTemperature(self.profile)

    def learnDirection(self, state: float):
        if state < self.min:
            self.actionMatrix[random.randint(0, len(self.actionMatrix) - 1)] = 1
        elif state > self.max:
            self.actionMatrix[random.randint(0, len(self.actionMatrix) - 1)] = -1
        else:
            self.actionMatrix[random.randint(0, len(self.actionMatrix) - 1)] = 0

class TemperatureGUI(tk.Tk):
    def __init__(self, ai_model):
        super().__init__()
        self.title("House Temperature Monitor")

        self.temperature_label = Label(self, text="Current Temperature: N/A")
        self.temperature_label.pack(pady=20)

        self.action_label = Label(self, text="AI Action: N/A")
        self.action_label.pack(pady=20)

        self.ai_model = ai_model
        self.update_display()

    def update_display(self):
        # Get the latest temperature from the database
        current_temperature = Database().getTargetTemperature()

        # Update the label with the latest temperature
        if current_temperature is not None:
            self.temperature_label.config(text=f"Current Temperature: {current_temperature} °C")
        else:
            self.temperature_label.config(text="Error fetching temperature data")

        # Get the latest AI action from the model
        current_action = self.ai_model.actionMatrix[0]  # Assuming actionMatrix has a single value for simplicity

        # Update the label with the latest AI action
        self.action_label.config(text=f"AI Action: {current_action}")

        # Schedule the next update after 5000 milliseconds (5 seconds)
        self.after(5000, self.update_display)

def simulation():
    model = AiModel()
    model.setProfile()
    current_temperature = Controller().getTargetTemperature()

    # Start the Tkinter GUI in a separate thread
    gui_thread = threading.Thread(target=start_gui, args=(model,))
    gui_thread.start()

    while True:
        time.sleep(1 / 100)
        print(model.actionMatrix)
        print(model.min)
        print(model.max)
        print(current_temperature)
        action = random.choice(model.actionMatrix)
        if action == 1:
            Controller().setTargetTemperature(current_temperature + 1)
        elif action == -1:
            Controller().setTargetTemperature(current_temperature - 1)
        model.learnDirection(current_temperature)
        current_temperature = Controller().getTargetTemperature()

def start_gui(ai_model):
    app = TemperatureGUI(ai_model)
    app.mainloop()

if __name__ == "__main__":
    simulation()
