import tkinter as tk
from tkinter import ttk
from class_network_client import Client
import sqlite3

class SmartThermostatApp(tk.Tk):
    def __init__(self, client):
        super().__init__()

        self.title("Smart AI Thermostat")
        self.geometry("480x320")

        self.profile_names = self.fetch_profile_names()

        self.profile_label = ttk.Label(self, text="Select Profile:")
        self.profile_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.profile_combobox = ttk.Combobox(self, values=self.profile_names)
        self.profile_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.profile_combobox.set("")

        self.fetch_profiles_button = ttk.Button(self, text="Select:", command=self.fetch_profiles)
        self.fetch_profiles_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.save_changes_button = ttk.Button(self, text="Save Changes", command=self.save_changes)
        self.save_changes_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.client = client
        self.update_temperature()

    def fetch_profile_names(self):
        connection = sqlite3.connect("profiles.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS profiles (name TEXT, max_temp REAL, min_temp REAL, ac_mode TEXT, ai_sensitivity REAL)")
        connection.commit()

        cursor.execute("SELECT name FROM profiles")
        profile_names = [row[0] for row in cursor.fetchall()]

        connection.close()
        return profile_names

    def fetch_profiles(self):
        selected_profile = self.profile_combobox.get()
        if selected_profile:
            connection = sqlite3.connect("profiles.db")
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM profiles WHERE name=?", (selected_profile,))
            profile_data = cursor.fetchone()

            connection.close()

            if profile_data:
                print(f"Fetched Profile: {profile_data}")
            else:
                print(f"Profile not found: {selected_profile}")
        else:
            print("Select a profile first.")

    def save_changes(self):
        selected_profile = self.profile_combobox.get()
        if selected_profile:
            print(f"Changes saved for {selected_profile}")
        else:
            print("Select a profile first.")

    def update_temperature(self):
        #self.get_average_temperature()
        #self.get_average_humidity()
        #self.get_feels_like_temperature()
        self.after(1000, self.update_temperature)

if __name__ == '__main__':
    client = Client()
    client.connectToServer()

    app = SmartThermostatApp(client)
    app.mainloop()
