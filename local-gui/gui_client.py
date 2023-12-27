import tkinter as tk
from tkinter import ttk
from class_network_client import *

class SmartThermostatApp(tk.Tk):
    def __init__(self, client):
        super().__init__()

        self.title("Smart AI Thermostat")
        self.geometry("300x100")
        
        self.average_temperature = 0.0
        self.average_humidity = 0.0
        self.feels_like_temperature = 0.0

        self.temperature_label = ttk.Label(self, text=f"Temperature: {self.feels_like_temperature}°F", font=("Arial", 14))
        self.temperature_label.pack(pady=10)

        self.client = client
        self.updateTemperature()

    def getAverageTemperature(self):
        self.client.sendReadFlag(self.client)
        self.client.sendData("SELECT AVG(temperature) FROM sensor WHERE temperature IS NOT NULL AND (id, timestamp) IN (SELECT id, MAX(timestamp) as max_timestamp FROM sensor WHERE temperature IS NOT NULL GROUP BY id);")
        self.tuple_average_temperature = eval(self.client.getData())
        self.average_temperature = self.tuple_average_temperature[0]
        print("AVERAGE TEMPERATURE CAPTURED")

    def getAverageHumidity(self):
        self.client.sendReadFlag(self.client)
        self.client.sendData("SELECT AVG(humidity) FROM sensor WHERE humidity IS NOT NULL AND (id, timestamp) IN (SELECT id, MAX(timestamp) as max_timestamp FROM sensor WHERE humidity IS NOT NULL GROUP BY id);")
        self.tuple_average_humidity = eval(self.client.getData())
        self.average_humidity = self.tuple_average_humidity[0]
        print("AVERAGE HUMIDITY CAPTURED")

    def getFeelsLikeTemperature(self):
        self.coefficients = [-42.379, 2.04901523, 10.14333127, -0.22475541, -6.83783e-3,
            -5.481717e-2, 1.22874e-3, 8.5282e-4, -1.99e-6]
        
        self.relative_humidity = self.average_humidity / 100.0

        self.feels_like_temperature = self.coefficients[0] + self.coefficients[1] * self.average_temperature + self.coefficients[2] * self.relative_humidity + \
                    self.coefficients[3] * self.average_temperature  * self.relative_humidity + self.coefficients[4] * self.average_temperature **2 + \
                    self.coefficients[5] * self.relative_humidity**2 + self.coefficients[6] * self.average_temperature **2 * self.relative_humidity + \
                    self.coefficients[7] * self.average_temperature  * self.relative_humidity**2 + self.coefficients[8] * self.average_temperature **2 * self.relative_humidity**2
        print("FEELS LIKE TEMPERATURE CALCULATED")

    def updateTemperature(self):
        self.getAverageTemperature()
        self.getAverageHumidity()
        self.getFeelsLikeTemperature()
        self.temperature_label.config(text=f"Temperature: {self.feels_like_temperature}°F")

        self.after(1, self.updateTemperature)

        # sending shit to db
    current_profile_data = self.getCurrentProfileData()
    change_in_thermostat_data = self.getChangeInThermostatData()

    self.client.sendReadFlag(self.client)

    if current_profile_data != "nothing" and change_in_thermostat_data != "nothing":
        query = f"INSERT INTO Gui (current_profile, change_in_thermostat) VALUES ({current_profile_data}, {change_in_thermostat_data})"
        self.client.sendData(query)
    # I DONT UNDERSTAND
    

if __name__ == '__main__':
    client = Client()
    client.connectToServer()

    app = SmartThermostatApp(client)
    app.mainloop()
