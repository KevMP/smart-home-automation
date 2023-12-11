from model import Model
import time
import tkinter as tk
from tkinter import font

class Simulation:
    def __init__(self):
        self.lower_bound = 70 - 2
        self.upper_bound = 71 + 2
        self.current_temperature = self.lower_bound
        self.previous_temperature = self.current_temperature
        self.preferred_temperatures = [70, 71]

    def getCurrentTemperature(self):
        return self.current_temperature

    def setCurrentTemperature(self, action: int):
        self.previous_temperature = self.current_temperature
        if action == 1:
            self.current_temperature += 1
        elif action == -1:
            self.current_temperature -= 1

        self.current_temperature = max(self.lower_bound, min(self.current_temperature, self.upper_bound))

    def getDirection(self):
        return self.current_temperature - self.previous_temperature

    def isAiGettingCloserToTarget(self):
        if self.current_temperature > self.preferred_temperatures[0] and self.current_temperature < self.preferred_temperatures[1]:
            if self.getDirection() == 0:
                return 1
            else:
                return -1
        elif self.current_temperature < self.preferred_temperatures[0]:
            if self.getDirection() == 1:
                return 1
            else:
                return -1
        elif self.current_temperature > self.preferred_temperatures[1]:
            if self.getDirection() == -1:
                return 1
            else:
                return -1

    def increasePreferredTemperature(self):
        self.preferred_temperatures = [temp + 1 for temp in self.preferred_temperatures]
        self.lower_bound = self.preferred_temperatures[0] - 2
        self.upper_bound = self.preferred_temperatures[1] + 2

    def decreasePreferredTemperature(self):
        self.preferred_temperatures = [temp - 1 for temp in self.preferred_temperatures]
        self.lower_bound = self.preferred_temperatures[0] - 2
        self.upper_bound = self.preferred_temperatures[1] + 2


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Temperature Monitor")
        self.master.geometry("500x500")

        # Set a larger font for the temperature label
        self.temperature_font = font.Font(family="Helvetica", size=20)

        self.temperature_label = tk.Label(master, text="Current Temperature: 0", font=self.temperature_font)
        self.temperature_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.increase_button = tk.Button(master, text="Increase Temperature", command=self.increase_temperature)
        self.increase_button.grid(row=1, column=0, padx=10, pady=10)

        self.decrease_button = tk.Button(master, text="Decrease Temperature", command=self.decrease_temperature)
        self.decrease_button.grid(row=1, column=1, padx=10, pady=10)

        self.ai = Model()
        self.environment = Simulation()
        self.CYCLE_SPEED = 1 / 100

        self.update_temperature()

    def update_temperature(self):
        self.temperature_label.config(text=f"Current Temperature: {self.environment.getCurrentTemperature()}")
        self.master.after(10, self.update_temperature)

    def run_simulation(self):
        action = self.ai.getAction()
        self.environment.setCurrentTemperature(action)
        self.ai.reward(self.environment.isAiGettingCloserToTarget())
        self.master.after(int(self.CYCLE_SPEED * 1000), self.run_simulation)

    def increase_temperature(self):
        self.environment.increasePreferredTemperature()

    def decrease_temperature(self):
        self.environment.decreasePreferredTemperature()


def main():
    root = tk.Tk()
    app = App(root)
    root.after(int(app.CYCLE_SPEED * 1000), app.run_simulation)
    root.mainloop()


if __name__ == "__main__":
    main()
