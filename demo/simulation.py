from model import Model
import time
import tkinter as tk

class Simulation:
    def __init__(self):
        self.current_temperature = 0
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


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Temperature Monitor")
        self.master.geometry("500x500")

        self.temperature_label = tk.Label(master, text="Current Temperature: 0")
        self.temperature_label.pack()

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


def main():
    root = tk.Tk()
    app = App(root)
    root.after(int(app.CYCLE_SPEED * 1000), app.run_simulation)
    root.mainloop()


if __name__ == "__main__":
    main()
