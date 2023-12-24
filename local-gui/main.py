import tkinter as tk
from tkinter import ttk, simpledialog
import sqlite3
from class_network_client import *

class SmartThermostatApp(tk.Tk):
    def __init__(self, client):
        super().__init__()
        self.client = client

        self.title("Smart AI Thermostat")
        self.geometry("400x300")

        self.average_temperature = 0
        self.average_humidity = 0
        self.feels_like_temperature = 72
        self.notification_messages = ["Welcome", "AC Unit Running Smoothly", "Filter Needs Replacement"]
        self.current_message_index = 0

        self.notification_label = ttk.Label(self, text="Notification message here", font=("Arial", 12))
        self.notification_label.pack(pady=10)

        self.temperature_label = ttk.Label(self, text=f"Temperature: {self.feels_like_temperature}°F", font=("Arial", 14))
        self.temperature_label.pack(pady=10)

        self.slider = ttk.Scale(self, from_=60, to=80, orient="horizontal", length=200, command=self.update_temperature)
        self.slider.set(self.feels_like_temperature)
        self.slider.pack(pady=10)

        self.increase_button = ttk.Button(self, text="Increase Temperature", command=self.increase_temperature)
        self.increase_button.pack(pady=10)

        self.decrease_button = ttk.Button(self, text="Decrease Temperature", command=self.decrease_temperature)
        self.decrease_button.pack(pady=10)

        self.create_profile_button = ttk.Button(self, text="Create Profile", command=self.create_profile)
        self.create_profile_button.pack(pady=10)

        self.manage_profiles_button = ttk.Button(self, text="Manage Profiles", command=self.show_profile_screen)
        self.manage_profiles_button.pack(pady=10)

        self.notification_animation()
    
    """
    The following is used to calculate the feels like temperature, therefore this Gui needs
    to collect the average temperature, and the average humidity.
    """
    def getAverageTemperature(self):
        return "SELECT AVG(temperature) FROM sensor WHERE temperature IS NOT NULL AND (id, timestamp) IN (SELECT id, MAX(timestamp) as max_timestamp FROM sensor WHERE temperature IS NOT NULL GROUP BY id);"
    def getAverageHumidity(self):
        return "SELECT AVG(humidity) FROM sensor WHERE humidity IS NOT NULL AND (id, timestamp) IN (SELECT id, MAX(timestamp) as max_timestamp FROM sensor WHERE humidity IS NOT NULL GROUP BY id);"
    def calculateFeelsLikeTemperature(self):
        self.coefficients = [-42.379, 2.04901523, 10.14333127, -0.22475541, -6.83783e-3,
            -5.481717e-2, 1.22874e-3, 8.5282e-4, -1.99e-6]
        
        self.relative_humidity = self.average_humidity / 100.0

        self.feels_like_temperature = self.coefficients[0] + self.coefficients[1] * self.average_temperature + self.coefficients[2] * self.relative_humidity + \
                    self.coefficients[3] * self.average_temperature  * self.relative_humidity + self.coefficients[4] * self.average_temperature **2 + \
                    self.coefficients[5] * self.relative_humidity**2 + self.coefficients[6] * self.average_temperature **2 * self.relative_humidity + \
                    self.coefficients[7] * self.average_temperature  * self.relative_humidity**2 + self.coefficients[8] * self.average_temperature **2 * self.relative_humidity**2
        
    def update_temperature(self):
        self.client.sendReadFlag(client)
        self.average_temperature = eval(self.client.getData())
        self.average_temperature = self.average_temperature[0]

        self.client.sendReadFlag(client)
        self.average_humidity = eval(self.client.getData())
        self.average_humidity = self.average_humidity[0]

        self.feels_like_temperature = self.feels_like_temperature
        self.temperature_label.config(text=f"Temperature: {self.feels_like_temperature}°F")

    def increase_temperature(self):
        """
        This will make a query to increase the profile min/max temperature,
        this is so that the Ai will make note of the change, and therefore
        try to correct the air conditioner.
            query =
                UPDATE Profile
                SET min_temp = min_temp + 1, max_temp = max_temp + 1
                WHERE name = ?;
        """
        self.feels_like_temperature += 1
        self.slider.set(self.feels_like_temperature)
    def decrease_temperature(self):
        self.feels_like_temperature -= 1
        self.slider.set(self.feels_like_temperature)
    """
    Profile needs to be created with a minimum and maximum temperature.
    """
    def save_profile_to_db(self, profile_name):
        return f"INSERT INTO Profile VALUES ('{profile_name}', {self.min_temp}, {self.max_temp});"
    def create_profile(self):
        profile_name = simpledialog.askstring("Create Profile", "Enter profile name:")
        if profile_name:
            self.save_profile_to_db(profile_name)
            print(f'Profile "{profile_name}" created with temperature {self.feels_like_temperature}°F')

    def notification_animation(self):
        self.notification_label.config(text=self.notification_messages[self.current_message_index])
        self.current_message_index = (self.current_message_index + 1) % len(self.notification_messages)
        self.after(2000, self.notification_animation)

    def show_profile_screen(self):
        profile_screen = ProfileScreen(self)
        profile_screen.grab_set() 
        profile_screen.wait_window()


class ProfileScreen(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Manage Profiles")
        self.geometry("300x200")

        self.master = master

        self.profile_listbox = tk.Listbox(self)
        self.profile_listbox.pack(pady=10)

        self.load_profiles()

        self.delete_button = ttk.Button(self, text="Delete Profile", command=self.delete_profile)
        self.delete_button.pack(pady=10)

        self.ok_button = ttk.Button(self, text="OK", command=self.destroy)
        self.ok_button.pack(pady=10)

    def getProfiles(self):
        return "SELECT name FROM Profile"
    def load_profiles(self):
        self.client.waitForServerContinueFlag(self.client)
        self.client.sendReadFlag(self.client)

        self.client.sendData(self.getProfiles())
        self.profiles = eval(self.client.getData())

        for profile in self.profiles:
            self.profile_listbox.insert(tk.END, profile[0])

    def delete_profile(self):
        selected_profile_index = self.profile_listbox.curselection()
        if selected_profile_index:
            selected_profile_name = self.profile_listbox.get(selected_profile_index)

            self.client.waitForServerContinueFlag(self.client)
            self.client.sendWriteFlag(self.client)

            self.deleteProfile(selected_profile_name)
            self.profile_listbox.delete(selected_profile_index)

    def deleteProfile(self, profile_name):
        return f"DELETE FROM Profile where name = '{profile_name}';"

if __name__ == '__main__':
    client = Client()
    client.connectToServer()

    app = SmartThermostatApp(client)
    app.mainloop()
