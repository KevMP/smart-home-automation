from model import Model
from sensor import Sensor
import random
import tkinter as tk
from tkinter import font

class Simulation:
    def __init__(self, num_sensors=6):  # Increase the number of sensors
        self.lower_bound = 70 - 2
        self.upper_bound = 71 + 2
        self.current_temperature = self.lower_bound
        self.previous_temperature = self.current_temperature
        self.preferred_temperatures = [70, 71]
        self.sensors = [Sensor(distance_from_temperature_source=2.0) for _ in range(num_sensors)]
        self.cycles = 0

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

    def updateSensors(self):
        for sensor in self.sensors:
            if self.cycles % sensor.distance_from_temperature_source == 0:
                temperature_modifier = random.uniform(-1, 1)
                sensor.setTemperatureModifier(temperature_modifier)
                sensor.temperature += temperature_modifier
                sensor.temperature = max(self.lower_bound, min(sensor.temperature, self.upper_bound))

    def getSensorTemperatures(self):
        return [sensor.temperature for sensor in self.sensors]

    def increasePreferredTemperature(self):
        self.preferred_temperatures = [temp + 1 for temp in self.preferred_temperatures]
        self.lower_bound = self.preferred_temperatures[0] - 2
        self.upper_bound = self.preferred_temperatures[1] + 2

    def decreasePreferredTemperature(self):
        self.preferred_temperatures = [temp - 1 for temp in self.preferred_temperatures]
        self.lower_bound = self.preferred_temperatures[0] - 2
        self.upper_bound = self.preferred_temperatures[1] + 2

    def incrementCycles(self):
        self.cycles += 1

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Temperature Monitor")
        self.master.geometry("400x300")

        # Set a larger font for the temperature label
        self.temperature_font = font.Font(family="Helvetica", size=20)

        self.ai = Model()
        self.environment = Simulation(num_sensors=9)  # Increase the number of sensors

        self.temperature_label = tk.Label(master, text="Current Temperature: 0", font=self.temperature_font)
        self.temperature_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.increase_button = tk.Button(master, text="Increase Temperature", command=self.increase_temperature)
        self.increase_button.grid(row=1, column=0, padx=10, pady=10)

        self.decrease_button = tk.Button(master, text="Decrease Temperature", command=self.decrease_temperature)
        self.decrease_button.grid(row=1, column=1, padx=10, pady=10)

        # Frame for sensor labels
        self.sensor_frame = tk.Frame(master, borderwidth=2, relief="groove")
        self.sensor_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # Labels to display individual sensor temperatures
        self.sensor_labels = [tk.Label(self.sensor_frame, text=f"Sensor {i+1}: 0.00") for i in range(len(self.environment.sensors))]
        for i, label in enumerate(self.sensor_labels):
            # Arrange sensors in pairs, stacked vertically
            row = i // 2
            col = i % 2
            label.grid(row=row, column=col, pady=5)

        self.CYCLE_SPEED = 1 / 100

        self.update_temperature()

    def update_temperature(self):
        self.environment.updateSensors()
        current_temperature = self.environment.getCurrentTemperature()
        self.temperature_label.config(text=f"Temperature: {current_temperature:.2f} F")

        # Update individual sensor labels
        sensor_temperatures = self.environment.getSensorTemperatures()
        for i, label in enumerate(self.sensor_labels):
            label.config(text=f"Sensor {i + 1}: {sensor_temperatures[i]:.2f} F")

        self.environment.incrementCycles()
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
